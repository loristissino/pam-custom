#!/usr/bin/env python

'''
    pam-custom
    Copyright (C) 2013 Loris Tisisno <loris.tissino@gmail.com>

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''

import os

def custom_auth(user, password, command):
  return os.system(command + ' ' + user + ' ' + password) == 0

def pam_sm_authenticate(pamh, flags, argv):

# the basic idea for getting the password via pam.conversation comes from
# http://benctechnicalblog.blogspot.it/2011/05/pam-python-module-for-out-of-band.html

  try:
    user = pamh.get_user(None)
    if user == None:
      return pamh.PAM_AUTH_ERR

    password = pamh.authtok
    if password == None:
      ## got no password in authtok - trying through conversation...
      passmsg = pamh.Message(pamh.PAM_PROMPT_ECHO_OFF, "Custom auth: ")
      rsp = pamh.conversation(passmsg)
      password = rsp.resp
      # so we should at this point have the password either through the
      # prompt or from previous module

    if custom_auth(user, password, argv[1]):
      return pamh.PAM_SUCCESS
    else:
      return pamh.PAM_AUTH_ERR

  except pamh.exception, e:
    return e.pam_result

def pam_sm_setcred(pamh, flags, argv):
  return pamh.PAM_SUCCESS

def pam_sm_acct_mgmt(pamh, flags, argv):
  return pamh.PAM_SUCCESS

def pam_sm_open_session(pamh, flags, argv):
  return pamh.PAM_SUCCESS

def pam_sm_close_session(pamh, flags, argv):
  return pamh.PAM_SUCCESS

def pam_sm_chauthtok(pamh, flags, argv):
  return pamh.PAM_SUCCESS

#!/usr/bin/python

import subprocess

from ansible.module_utils.basic import *

DOCUMENTATION = r'''
module: developer_mode
short_description: Manage OSX developer mode
description:
    - Enable and disable OSX developer mode
options:
    state:
        description:
            - Whether OSX developer mode is enabled or disabled, taking action if the state is different from what is stated.
        type: str
        choices: [ enable, disable ]
        default: enable
author:
- Ivan Spasov (@ispasov)
'''

EXAMPLES = r'''
- name: Enable OSX developer mode
  devtools_security:
    state: enable
- name: Disable OSX developer mode
  devtools_security:
    state: disable
'''

def run_devtools_security(module, flag):
    return module.run_command(['DevToolsSecurity', '-{}'.format(flag)])

def main():
    module = AnsibleModule(
        argument_spec=dict(
            state=dict(default='enable', choices=['enable', 'disable']),
        ),
        supports_check_mode=False,
    )

    status_output = run_devtools_security(module, 'status')

    enabled = 'enabled' in status_output[1]
    state = module.params['state']
    changed = False

    if state == 'enable' and not enabled or state == 'disable' and enabled:
        run_devtools_security(module, state)
        changed = True

    module.exit_json(changed=changed)

if __name__ == '__main__':
    main()
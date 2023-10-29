Powerline Full
**************

.. contents::
   :local:

An extension of the :doc:`powerline` theme, ``powerline_full`` includes all data
sources that Liquid Prompt provides. The ordering is the same as the default
theme.

.. versionadded:: 1.0

Preview
=======

If there is nothing special about the current context, the appearance of
Powerline might be as simple as this:

.. image:: images/powerline_full-short.png
   :alt:  user  ~  

If you are running a background command and are also in the "main" branch of a
Git repository on a server:

.. image:: images/powerline_full-med.png
   :alt:  1&  user   server  ~  liquidprompt  main  

When Liquid Prompt is displaying nearly everything, it may look like this:

.. image:: images/powerline_full-long.png
   :alt:  🕤  ⌁24%  ⌂1.68  θ90°  3d/2&/1z  user   server  ~   …   
       liquidprompt   …   theme  ⚞3  (e) pyenv  main(+10/-5,+3/-1)+*  20s 
        125  

Configuration
=============

Liquid Prompt Configuration
---------------------------
All Liquid Prompt config options are respected, **except for**:

* :attr:`LP_COLOR_AWS_PROFILE`
* :attr:`LP_COLOR_CONTAINER`
* :attr:`LP_COLOR_DIRSTACK`
* :attr:`LP_COLOR_ERR`
* :attr:`LP_COLOR_HOST`
* :attr:`LP_COLOR_IN_MULTIPLEXER`
* :attr:`LP_COLOR_JOB_D`
* :attr:`LP_COLOR_JOB_R`
* :attr:`LP_COLOR_JOB_Z`
* :attr:`LP_COLOR_KUBECONTEXT`
* :attr:`LP_COLOR_MARK_ROOT`
* :attr:`LP_COLOR_MARK_SUDO`
* :attr:`LP_COLOR_MARK`
* :attr:`LP_COLOR_NODE_VENV`
* :attr:`LP_COLOR_NOWRITE`
* :attr:`LP_COLOR_PATH_ROOT`
* :attr:`LP_COLOR_PATH`
* :attr:`LP_COLOR_PROXY`
* :attr:`LP_COLOR_RUBY_VENV`
* :attr:`LP_COLOR_RUNTIME`
* :attr:`LP_COLOR_SHLVL`
* :attr:`LP_COLOR_SSH`
* :attr:`LP_COLOR_SU`
* :attr:`LP_COLOR_TELNET`
* :attr:`LP_COLOR_TERRAFORM`
* :attr:`LP_COLOR_TIME`
* :attr:`LP_COLOR_USER_ALT`
* :attr:`LP_COLOR_USER_LOGGED`
* :attr:`LP_COLOR_USER_ROOT`
* :attr:`LP_COLOR_VIRTUALENV`
* :attr:`LP_COLOR_WRITE`
* :attr:`LP_COLOR_X11_OFF`
* :attr:`LP_COLOR_X11_ON`
* :attr:`LP_ENABLE_PERM`
* :attr:`LP_ENABLE_SSH_COLORS`
* :attr:`LP_ENABLE_SUDO`
* :attr:`LP_MARK_BRACKET_CLOSE`
* :attr:`LP_MARK_BRACKET_OPEN`
* :attr:`LP_MARK_BZR`
* :attr:`LP_MARK_DEFAULT`
* :attr:`LP_MARK_DISABLED`
* :attr:`LP_MARK_FOSSIL`
* :attr:`LP_MARK_GIT`
* :attr:`LP_MARK_HG`
* :attr:`LP_MARK_PERM`
* :attr:`LP_MARK_PREFIX`
* :attr:`LP_MARK_PROXY`
* :attr:`LP_MARK_SVN`
* :attr:`LP_MARK_VCSH`

Theme Configuration
-------------------

Powerline Full uses all the config options of the :doc:`powerline` theme,
**except for**:

* :attr:`POWERLINE_STASH_MARKER`
* :attr:`POWERLINE_VCS_DIRTY_COLOR`
* :attr:`POWERLINE_VCS_MARKER`
* :attr:`POWERLINE_VCS_STASH_COLOR`

Powerline Full adds these config options:

Markers
_______

.. attribute:: POWERLINE_AWS_PROFILE_MARKER
   :type: string
   :value: "AWS: "

   The marker string used to indicate the following string is the name of an
   AWS profile.

.. attribute:: POWERLINE_CHROOT_MARKER
   :type: string
   :value: "chroot: "

   The marker string used to indicate the following string is a chroot.

.. attribute:: POWERLINE_KUBECONTEXT_MARKER
   :type: string
   :value: $LP_MARK_KUBECONTEXT

   The marker string used to indicate the following string is the name of a
   ``kubectl`` context.

.. attribute:: POWERLINE_NODE_ENV_MARKER
   :type: string
   :value: "node: "

   The marker string used to indicate the following string is a Node.js
   environment.

.. attribute:: POWERLINE_PROXY_MARKER
   :type: string
   :value: "proxy: "

   The marker string used to indicate the following string is a HTTP proxy.

.. attribute:: POWERLINE_RUBY_ENV_MARKER
   :type: string
   :value: "ruby: "

   The marker string used to indicate the following string is a Ruby
   environment.

.. attribute:: POWERLINE_SOFTWARE_COLLECTION_MARKER
   :type: string
   :value: "(sc) "

   The marker string used to indicate the following string is a Red Hat Software
   Collection.

.. attribute:: POWERLINE_TERRAFORM_ENV_MARKER
   :type: string
   :value: "(tf) "

   The marker string used to indicate the following string is a Terraform
   workspace.

Colors
______

.. note::
   Arrays are set without commas (``,``). The default values are displayed with
   commas for clarity.

.. attribute:: POWERLINE_AWS_PROFILE_COLOR
   :type: array<int>
   :value: (190, 236, 0, 0, 3, 0)

   Color for the AWS profile section.

.. attribute:: POWERLINE_BATTERY_COLOR
   :type: array<int>
   :value: (-1, 238, 0, 0, -1, 0)

   Color for the battery section.

.. attribute:: POWERLINE_CHROOT_COLOR
   :type: array<int>
   :value: (219, 30, 0, 0, 7, 4)

   Color for the chroot section.

.. attribute:: POWERLINE_CONTAINER_COLOR
   :type: array<int>
   :value: $POWERLINE_NEUTRAL_COLOR

   Color for the container indicator section.

.. attribute:: POWERLINE_DIRSTACK_COLOR
   :type: array<int>
   :value: $POWERLINE_NEUTRAL_COLOR

   Color for the directory stack section.

.. attribute:: POWERLINE_KUBECONTEXT_COLOR
   :type: array<int>
   :value: (231, 74, 0, 0, 7, 4)

   Color for the Kubernetes context section.

.. attribute:: POWERLINE_LOAD_COLOR
   :type: array<int>
   :value: (-1, 148, 0, 0, -1, 3)

   Color for the CPU load section.

.. attribute:: POWERLINE_NEUTRAL_COLOR
   :type: array<int>
   :value: (252, 234, 0, 0, 7, 0)

   Color for all neutral sections, :attr:`LP_PS1_PREFIX` and
   :attr:`LP_PS1_POSTFIX`.

.. attribute:: POWERLINE_NODE_ENV_COLOR
   :type: array<int>
   :value: $POWERLINE_PYTHON_ENV_COLOR

   Color for the Node.js environment section.

.. attribute:: POWERLINE_PROXY_COLOR
   :type: array<int>
   :value: (21, 219, 1, 0, 4, 7)

   Color for the HTTP proxy section.

.. attribute:: POWERLINE_RUBY_ENV_COLOR
   :type: array<int>
   :value: $POWELINE_PYTHON_ENV_COLOR

   Color for the Ruby environment section.

.. attribute:: POWERLINE_RUNTIME_COLOR
   :type: array<int>
   :value: (226, 17, 0, 0, 3, 4)

   Color for the command runtime section.

.. attribute:: POWERLINE_SHLVL_COLOR
   :type: array<int>
   :value: (231, 58, 0, 0, 7, 2)

   Color for the nested shell level section.

.. attribute:: POWERLINE_SOFTWARE_COLLECTIONS_COLOR
   :type: array<int>
   :value: (231, 62, 0, 0, 7, 5)

   Color for the Red Hat Software Collections section.

.. attribute:: POWERLINE_TEMPERATURE_COLOR
   :type: array<int>
   :value: (-1, 240, 0, 0, -1, 0)

   Color for the temperature section.

.. attribute:: POWERLINE_TERRAFORM_ENV_COLOR
   :type: array<int>
   :value: (231, 182, 0, 0, 7, 4)

   Color for the Terraform workspace.

.. attribute:: POWERLINE_TIME_COLOR
   :type: array<int>
   :value: (33, 17, 0, 0, 5, 4)

   Color for the current time section.

.. attribute:: POWERLINE_WIFI_STRENGTH_COLOR
   :type: array<int>
   :value: (-1, 148, 0, 0, -1, 3)

   Color for the wireless signal strength section.

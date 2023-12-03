Powerline
*********

The ``powerline`` theme is a clone of the `Powerline prompt`_. It copies the
`default segments`_ of the Powerline prompt for Shell.

This prompt is a proof of (a specific) concept: that Liquid Prompt can do what
Powerline does, but faster.
That said, this is a fully usable theme.

.. versionadded:: 1.0

.. _`Powerline prompt`: https://github.com/powerline/powerline
.. _`default segments`: https://github.com/powerline/powerline/blob/2.8/powerline/config_files/themes/shell/default.json

Preview
=======

If there is nothing special about the current context, the appearance of
Powerline might be as simple as this:

.. image:: images/powerline-short.png
   :alt:  user  ~  

If you are running a background command and are also in the "main" branch of a
Git repository on a server:

.. image:: images/powerline-med.png
   :alt:   server  user  ~  liquidprompt  1   main  

When Liquid Prompt is displaying nearly everything, it may look like this:

.. image:: images/powerline-long.png
   :alt:   server  user  (e) pyenv  ~   …   liquidprompt   …   theme  
       3   main  ST 1  125  

.. note::
   The above "everything" image looks like it is missing some parts because this
   theme does not implement all data sources of Liquid Prompt. This is by design
   to clone basic Powerline. For a Powerline theme that does show all data
   sources, see :doc:`powerline_plus`.

Configuration
=============

Liquid Prompt Configuration
---------------------------
The following Liquid Prompt config options are respected:

* :attr:`LP_DISABLED_VCS_PATHS`
* :attr:`LP_ENABLE_BZR`
* :attr:`LP_ENABLE_COLOR`
* :attr:`LP_ENABLE_ERROR`
* :attr:`LP_ENABLE_FOSSIL`
* :attr:`LP_ENABLE_FQDN`
* :attr:`LP_ENABLE_GIT`
* :attr:`LP_ENABLE_HG`
* :attr:`LP_ENABLE_JOBS`
* :attr:`LP_ENABLE_RUNTIME_BELL`
* :attr:`LP_ENABLE_SCREEN_TITLE`
* :attr:`LP_ENABLE_SHORTEN_PATH`
* :attr:`LP_ENABLE_SVN`
* :attr:`LP_ENABLE_TITLE`
* :attr:`LP_ENABLE_VCS_ROOT`
* :attr:`LP_ENABLE_VIRTUALENV`
* :attr:`LP_HOSTNAME_ALWAYS`
* :attr:`LP_PATH_CHARACTER_KEEP`
* :attr:`LP_PATH_KEEP`
* :attr:`LP_PATH_LENGTH`
* :attr:`LP_PATH_METHOD`
* :attr:`LP_PATH_VCS_ROOT`
* :attr:`LP_RUNTIME_BELL_THRESHOLD`
* :attr:`LP_USER_ALWAYS`

Theme Configuration
-------------------

Powerline adds these config options:

Markers
_______

.. attribute:: POWERLINE_HARD_DIVIDER
   :type: string
   :value: ""  # U+E0B0

   The divider character between sections, defaults to the private character
   used in Powerline fonts that looks like a solid right arrow.

.. attribute:: POWERLINE_PYTHON_ENV_MARKER
   :type: string
   :value: "(e) "

   The marker string used to indicate the following string is a Python
   environment.

.. attribute:: POWERLINE_ROOT_MARKER
   :type: string
   :value: "#"

   The marker character used to indicate a root session.

.. attribute:: POWERLINE_SECURE_MARKER
   :type: string
   :value: ""  # U+E0A2

   The marker character used to indicate a SSH session, defaults to the
   private character used in Powerline fonts that looks like a lock.

.. attribute:: POWERLINE_SOFT_DIVIDER
   :type: string
   :value: ""  # U+E0B1

   The divider character between similar sections, defaults to the private
   character used in Powerline fonts that looks like a thin right arrow.

.. attribute:: POWERLINE_SPACER
   :type: string
   :value: " "  # U+00A0: non-breaking space

   The marker character used to pad sections, defaults to the
   non-breaking space character.

   To add more padding, add more spaces to this string.

   A non-breaking space is needed in some fonts to prevent multiple spaces from
   collapsing to one space, loosing the padding.

.. attribute:: POWERLINE_STASH_MARKER
   :type: string
   :value: "ST"

   The marker string used to indicate stashes exist in the VCS repository.

.. attribute:: POWERLINE_VCS_MARKER
   :type: string
   :value: ""  # U+E0A0

   The marker character used to indicate a VCS repository, defaults to the
   private character used in Powerline fonts that looks like a branching commit
   history.

Colors
______

These color config options take an array of integers, which are arguments to
:func:`lp_terminal_format`.

.. note::
   Arrays are set without commas (``,``). The default values are displayed with
   commas for clarity.

.. attribute:: POWERLINE_ERROR_COLOR
   :type: array<int>
   :value: (231, 52, 0, 0, 7, 1)

   Color for the error code section.

.. attribute:: POWERLINE_HOST_COLOR
   :type: array<int>
   :value: (220, 166, 0, 0, 3, 2)

   Color for the hostname section.

.. attribute:: POWERLINE_JOBS_COLOR
   :type: array<int>
   :value: (220, 166, 0, 0, 3, 2)

   Color for the shell jobs section.

.. attribute:: POWERLINE_PATH_COLOR
   :type: array<int>
   :value: (250, 240, 0, 0, 7, 0)

   Color for the current working directory section.

.. attribute:: POWERLINE_PATH_LAST_COLOR
   :type: array<int>
   :value: (252, 240, 1, 0, 7, 0)

   Color for the current working directory last subsection.

.. attribute:: POWERLINE_PATH_SEPARATOR_COLOR
   :type: array<int>
   :value: (245, 240, 0, 0, 7, 0)

   Color for the current working directory subsection separator.

.. attribute:: POWERLINE_PATH_SHORTENED_COLOR
   :type: array<int>
   :value: (245, 240, 0, 0, 7, 0)

   Color for any sections in the current working directory that are shortened to
   make the path fit in :attr:`LP_PATH_LENGTH`.

.. attribute:: POWERLINE_PATH_VCS_COLOR
   :type: array<int>
   :value: (147, 240, 1, 0, 4, 0)

   Color for the current working directory segment corresponding to the current
   VCS repository root directory.

   :attr:`LP_PATH_VCS_ROOT` must be enabled to have any effect.

.. attribute:: POWERLINE_PYTHON_ENV_COLOR
   :type: array<int>
   :value: (231, 74, 0, 0, 7, 4)

   Color for the Python environment section.

.. attribute:: POWERLINE_USER_COLOR
   :type: array<int>
   :value: (231, 31, 1, 0, 7, 6)

   Color for the username section.

.. attribute:: POWERLINE_VCS_CLEAN_COLOR
   :type: array<int>
   :value: (250, 236, 0, 0, 7, 0)

   Color for the VCS section if the repository is clean.

.. attribute:: POWERLINE_VCS_DIRTY_COLOR
   :type: array<int>
   :value: (220, 236, 0, 0, 3, 0)

   Color for the VCS section if the repository is not clean.

.. attribute:: POWERLINE_VCS_STASH_COLOR
   :type: array<int>
   :value: (220, 236, 0, 0, 3, 0)

   Color for the VCS stash subsection.

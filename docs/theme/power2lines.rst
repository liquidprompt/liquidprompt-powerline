Power2lines
***********

This ``power2line`` theme rearranges the sections of :doc:`powerline_plus`,
but on two rows instead of one.
That is, the data sections are displayed on a first row, and the interactive
prompt forms a second row.
This gives room for long command lines, and let the user find the prompt always
at the same location.


Preview
=======

If there is nothing special about the current context, the appearance of
Powerline might be as simple as this:

.. image:: images/power2lines-short.png

A slightly longer prompt with more data:

.. image:: images/power2lines-med.png

When Liquid Prompt is displaying nearly everything, it may look like this:

.. image:: images/power2lines-long.png


Setup & Configuration
=====================

This theme as the same core configuration than the :doc:`powerline_plus` theme.

Theme Configuration
-------------------

Colors
______

.. attribute:: POWERLINE_LINE_COLOR
   :type: array<int>
   :value: (240 -1 0 0 14 -1)

   Color of the decorative lines.


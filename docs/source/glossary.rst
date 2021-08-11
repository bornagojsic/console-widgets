Glossary
========


ConsoleWidget()
---------------

ConsoleWidget is the root object from which all others widgets are derived.

``ConsoleWidget( parameter=value, ... )``

.. list-table:: Parameters
   :widths: 25 25 75
   :header-rows: 1

   * - Parameter
     - Default
     - Description
   * - title
     - ""
     - The title of the widget.
   * - subtitle
     - ""
     - The subtitle of the widget.
   * - body
     - ""
     - The body of the widget.



ConsoleBox()
------------

ConsoleBox is a basic widget which is surronded by a :ref:`Box()<box>` object.

``ConsoleBox( parameter=value, ... )``

.. list-table:: Parameters
   :widths: 25 25 75
   :header-rows: 1

   * - Parameter
     - Default
     - Description
   * - title
     - ""
     - The title of the widget.
   * - subtitle
     - ""
     - The subtitle of the widget.
   * - body
     - ""
     - The body of the widget.
   * - box
     - Box()
     - The box surronding the widget.


.. _box:

Box()
-----

Box is an object for storing the symbols used for building a boy around the widgets.

``Box( parameter=value, ... )``

.. list-table:: Parameters
   :widths: 25 25 75
   :header-rows: 1

   * - Parameter
     - Default
     - Description
   * - horizontal_symbol
     - "─"
     - The symbol on the horizontal axis of the box.
   * - vertical_symbol
     - "│"
     - The symbol on the vertical axis of the box.
   * - full_intersection
     - "┼"
     - Intersection of a horizontal and a vetrical line.
   * - left_vertical
     - "├"
     - Intersection of the left vertical border with a horizontal line.
   * - right_vertical
     - "┤"
     - Intersection of the right vertical border with a horizontal line.
   * - upper_horizontal
     - "┬"
     - Intersection of the upper horizontal border with a vertical line.
   * - lower_horizontal
     - "┴"
     - Intersection of the lower horizontal border with a vertical line.
   * - upper_left
     - "┌"
     - The symbol of the upper left corner.
   * - upper_right
     - "┐"
     - The symbol of the upper right corner.
   * - lower_left
     - "└"
     - The symbol of the lower left corner.
   * - lower_right
     - "┘"
     - The symbol of the lower right corner.
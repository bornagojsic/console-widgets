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

ConsoleBox is a basic widget which is surronded by a box.

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
   * - theme
     - "default"
     - The box theme. There are the default, double, wide and :ref:`many more<box_themes>`.
   * - horizontal_margin
     - 0
     - The horizontal margin of the box.
   * - vertical_margin
     - 0
     - The vertical margin of the box.
   * - allignment
     - "CENTER"
     - Allignment of the text in the box
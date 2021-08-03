Glossary
========


ConsoleWidget()
---------------

ConsoleWidget is the root object from which all others widgets are derived.

``ConsoleWidget( parameter=value, ... )``

.. list-table:: Parameters
   :widths: 25 75
   :header-rows: 1

   * - Parameter
     - Description
   * - title
     - The title of the widget.
   * - subtitle
     - The subtitle of the widget.
   * - body
     - The body of the widget.



ConsoleBox()
------------

ConsoleBox is a basic widget which is surronded by a :ref:`Box()<box>` object.

``ConsoleBox( parameter=value, ... )``

.. list-table:: Parameters
   :widths: 25 75
   :header-rows: 1

   * - Parameter
     - Description
   * - title
     - The title of the widget.
   * - subtitle
     - The subtitle of the widget.
   * - body
     - The body of the widget.
   * - body
     - The box surronding the widget.


.. _box:

Box()
-----

Box is an object for storing the symbols used for building a boy around the widgets.

``Box( parameter=value, ... )``

.. list-table:: Parameters
   :widths: 25 75
   :header-rows: 1

   * - Parameter
     - Description
   * - horizontal_symbol
     - The symbol on the horizontal axis of the box.
   * - vertical_symbol
     - The symbol on the vertical axis of the box.
   * - corners
     - A list with the symbols for the corners in the following format: [upper_left, upper_right, lower_left, lower_right].
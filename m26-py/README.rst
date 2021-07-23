m26 - calculations for sports like running, cycling, and swimming
=================================================================

Features
--------

- Create Distances in either miles, kilometers, or yards.
- Translates Distances to the other units of measure.
- Specify ElapsedTime either in 'hh:mm:ss' strings, or int second values.
- Calculates Speed from a given Distance and ElapsedTime - per mile, per kilometer, and per yard.
- Calculates pace_per_mile and seconds_per_mile for a given Speed.
- Projects one Speed to another Distance with either a simple or algorithmic formula.
- RunWalkCalculator calculates pace and mph from given time intervals and paces.
- Calculates the Age of person, and age_graded times.
- Calculates five standard heart-rate training zones based on Age.


Quick start
-----------

Installation:

.. code-block:: console

    $ pip install m26

Use:

.. code-block:: pycon

    >>> import m26

    >>> d1 = m26.Distance(26.2)
    >>> d1
    <Distance value:26.2 uom:m>
    >>> d1.as_miles()
    26.2
    >>> d1.as_kilometers()
    42.1648128
    >>> d1.as_yards()
    46112.0

    >>> d2 = m26.Distance(50.0, m26.Constants.uom_kilometers())
    >>> d2
    <Distance value:50.0 uom:k>

    >>> d3 = m26.Distance(7040, m26.Constants.uom_yards())
    >>> d3
    <Distance value:7040.0 uom:y>

    >>> d4 = m26.Distance(10.0, m26.Constants.uom_kilometers())
    >>> d4.add(d1)
    >>> d4
    <Distance value:52.1648128 uom:k>
    >>> d4.subtract(d3)
    >>> d4
    <Distance value:45.7274368 uom:k>

    >>> t1 = m26.ElapsedTime('3:47:30')
    >>> t1
    <ElapsedTime hh:3.0 mm:47.0 ss:30.0 secs:13650.0>

    >>> t2 = m26.ElapsedTime(3662)
    >>> t2
    <ElapsedTime hh:1 mm:1 ss:2.0 secs:3662.0>

    >>> s = m26.Speed(d1, t1)
    >>> s
    <Speed dist:<Distance value:26.2 uom:m> etime:<ElapsedTime hh:3.0 mm:47.0 ss:30.0 secs:13650.0>>

    >>> s.mph()
    6.90989010989011

    >>> s.kph()
    11.120390189010989

    >>> s.yph()
    12161.406593406595

    >>> s.seconds_per_mile()
    520.9923664122138

    >>> s.pace_per_mile()
    '8:40.99'

    >>> s.projected_time(d2, 'simple')
    '04:29:46'

    >>> s.projected_time(d2, 'riegel')
    '04:32:32'

    >>> result = m26.RunWalkCalculator.calculate('2:30', '9:16', '0:45', '17:00', 31.0)
    >>> result
    {
      "avg_mph": 5.4292343387471,
      "avg_ppm": "11:03.07",
      "miles": 31.0,
      "proj_miles": 31.0,
      "proj_time": "05:42:35",
      "run_hhmmss": "2:30",
      "run_ppm": "9:16",
      "walk_hhmmss": "0:45",
      "walk_ppm": "17:00"
    }

    >>> a = m26.AgeCalculator.calculate('1960-10-01', '2015-10-18')
    >>> a
    <Age value:55.044490075290895>

    >>> a2 = m26.Age(58.1)
    >>> a2
    <Age value:58.1>

    >>> graded = s.age_graded(a, a2)
    >>> graded
    <Speed dist:<Distance value:26.2 uom:m> etime:<ElapsedTime hh:3 mm:51 ss:47.61402391772026 secs:13907.61402391772>>

    >>> zones = a2.training_zones()
    >>> zones
    [
      {
        "age": 58.1,
        "max": 161.9,
        "pct_max": 0.95,
        "pulse": 153.805,
        "zone": 1
      },
      {
        "age": 58.1,
        "max": 161.9,
        "pct_max": 0.9,
        "pulse": 145.71,
        "zone": 2
      },
      {
        "age": 58.1,
        "max": 161.9,
        "pct_max": 0.85,
        "pulse": 137.615,
        "zone": 3
      },
      {
        "age": 58.1,
        "max": 161.9,
        "pct_max": 0.8,
        "pulse": 129.52,
        "zone": 4
      },
      {
        "age": 58.1,
        "max": 161.9,
        "pct_max": 0.75,
        "pulse": 121.42500000000001,
        "zone": 5
      }
    ]


Source Code
===========

See `m26-py at GitHub <https://github.com/cjoakim/m26-py>`_ .


Changelog
=========

Version 0.2.1
-------------

-  2020/02/19. Version 0.2.1,  Jinja2 upgrade
-  2017/09/27. Version 0.2.0,  Converted to the pytest testing framework; coverage at 100%.
-  2015/10/31. Initial Production release.

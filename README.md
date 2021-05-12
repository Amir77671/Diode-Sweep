---
title: 'Diode sweep test'
disqus: hackmd
---

Diode sweep test
===

## Table of Contents

[TOC]

## Description

This LabVIEW program performs a sweet test on diodes connected to a supply and multimeter. Both supply and multimeter are controlled throught VISA.
Both LabVIEW and Python files perform the same test.

User manual
---


![](https://i.imgur.com/XoIey2M.png)

To correctly use the program, both the supply and multimeter GPIB adresses have to be entered in the block diagram.

![](https://i.imgur.com/EEmrNIv.png)

Front panel contains current and voltage indicators at the bottom aswell as number of iterations on the top left corner


Example
---
Figure below represents an example sweep test performed on a diode, 99 total iterations and maximum voltage = 1.08V


![](https://i.imgur.com/jfW91xB.png)


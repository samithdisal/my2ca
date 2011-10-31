#!/bin/bash

pyside-uic mainwindow.ui > ../ui_mainwindow.py
pyside-uic connectMySqlDlg.ui > ../ui_connectMySqlDlg.py
pyside-uic select_tables_page.ui > ../ui_select_tables_page.py

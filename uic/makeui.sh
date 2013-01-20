#!/bin/bash

pyside-uic mainwindow.ui > ../uigen.py
pyside-uic connectMySqlDlg.ui >> ../uigen.py
pyside-uic select_tables_page.ui >> ../uigen.py
pyside-uic preview_page.ui >> ../uigen.py

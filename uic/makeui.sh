#!/bin/bash

pyside-uic mainwindow.ui > ../uigen.py
pyside-uic connectMySqlDlg.ui >> ../uigen.py
pyside-uic select_tables_page.ui >> ../uigen.py
pyside-uic preview_page.ui >> ../uigen.py
pyside-uic progress_page.ui >> ../uigen.py
pyside-uic finalize_page.ui >> ../uigen.py


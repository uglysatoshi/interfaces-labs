#-------------------------------------------------
#
# Project created by QtCreator 2024-04-30T13:51:46
#
#-------------------------------------------------

QT       += core gui opengl

greaterThan(QT_MAJOR_VERSION, 4): QT += widgets

TARGET = OpenGL_Appl
TEMPLATE = app


SOURCES += main.cpp\
        mainwindow.cpp \
    glwidget.cpp

HEADERS  += mainwindow.h \
            glwidget.h

FORMS    += mainwindow.ui

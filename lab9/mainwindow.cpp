#include "mainwindow.h"
#include "ui_mainwindow.h"
#include <QtWidgets>
#include "glwidget.h"

MainWindow::MainWindow(QWidget *parent) : QMainWindow(parent),
ui(new Ui::MainWindow)
{
ui->setupUi(this);
connect(ui->slNewDraw, SIGNAL(valueChanged(int)),
ui->widget, SLOT(ChangeStructFunc(int)));

connect(ui->vsX, SIGNAL(valueChanged(int)), ui->widget, SLOT(ChangeX(int)));
connect(ui->vsY, SIGNAL(valueChanged(int)), ui->widget, SLOT(ChangeY(int)));
connect(ui->vsAngle, SIGNAL(valueChanged(int)), ui->widget, SLOT(ChangeAngle(int)));
}
MainWindow::~MainWindow()
{
    delete ui;
}

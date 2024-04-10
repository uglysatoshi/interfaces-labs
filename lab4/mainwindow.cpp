#include "mainwindow.h"
#include "ui_mainwindow.h"
#include <QAction>

MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow)
{
    ui->setupUi(this);
    ui->pushButton->setToolTip("Подсказка<BR><B>ПАСХАЛОЧКА</B>");
}

MainWindow::~MainWindow()
{
    delete ui;
}

void MainWindow::on_pushButton_clicked()
{
    ui->statusBar->showMessage("Message!!", 0);
}

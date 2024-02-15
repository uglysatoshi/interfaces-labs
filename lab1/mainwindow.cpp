#include "mainwindow.h"
#include "ui_mainwindow.h"
#include <cmath>

MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow)
{
    ui -> setupUi(this);
}



MainWindow::~MainWindow()
{
    delete ui;
}

void MainWindow::on_plus_clicked() {
    double x1 = ui-> line_1 -> text().toDouble();
    double x2 = ui-> line_2 -> text().toDouble();
    QString s;
    s.sprintf("%.4f", x1 + x2);
    ui -> result -> setText(s);
}

void MainWindow::on_multy_clicked() {
    double x1 = ui-> line_1 -> text().toDouble();
    double x2 = ui-> line_2 -> text().toDouble();
    QString s;
    s.sprintf("%.4f", x1 * x2);
    ui -> result -> setText(s);
}

void MainWindow::on_divide_clicked()
{
    double x1 = ui-> line_1 -> text().toDouble();
    double x2 = ui-> line_2 -> text().toDouble();
    QString s;
    s.sprintf("%.4f", x1 / x2);
    ui -> result -> setText(s);
}

void MainWindow::on_minus_clicked()
{
    double x1 = ui-> line_1 -> text().toDouble();
    double x2 = ui-> line_2 -> text().toDouble();
    QString s;
    s.sprintf("%.4f", x1-x2);
    ui -> result -> setText(s);
}

void MainWindow::on_sin_1_clicked()
{
    double x1 = ui-> line_1 -> text().toDouble();
    QString s;
    s.sprintf("%.4f", sin(x1));
    ui -> line_1 -> setText(s);
}

void MainWindow::on_sin_2_clicked() {
    double x2 = ui-> line_2 -> text().toDouble();
    QString s;
    s.sprintf("%.4f", sin(x2));
    ui -> line_2 -> setText(s);
}

void MainWindow::on_pow_1_clicked() {
    double x1 = ui-> line_1 -> text().toDouble();
    QString s;
    s.sprintf("%.4f", x1 * x1);
    ui -> line_1 -> setText(s);
}

void MainWindow::on_pow_2_clicked() {
    double x2 = ui-> line_2 -> text().toDouble();
    QString s;
    s.sprintf("%.4f", x2 * x2);
    ui -> line_2 -> setText(s);
}



void MainWindow::on_sqrt_1_clicked()
{
    double x1 = ui-> line_1 -> text().toDouble();
    QString s;
    s.sprintf("%.4f", sqrt(x1));
    ui -> line_1 -> setText(s);
}

void MainWindow::on_sqrt_2_clicked()
{
    double x2 = ui-> line_2 -> text().toDouble();
     QString s;
     s.sprintf("%.4f", sqrt(x2));
     ui -> line_2 -> setText(s);
}

void MainWindow::on_log_1_clicked()
{
    double x1 = ui-> line_1 -> text().toDouble();
     QString s;
     s.sprintf("%.4f", log(x1));
     ui -> line_1 -> setText(s);
}

void MainWindow::on_log_2_clicked()
{
    double x2 = ui-> line_2 -> text().toDouble();
     QString s;
     s.sprintf("%.4f", log(x2));
     ui -> line_2 -> setText(s);
}


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

void MainWindow::on_b1_clicked()
{
    QString s;
    s = ui -> expression -> text();
    ui -> expression -> setText(s+"1");
}

void MainWindow::on_b2_clicked()
{
    QString s;
    s = ui -> expression -> text();
    ui -> expression -> setText(s+"2");
}

void MainWindow::on_b3_clicked()
{
    QString s;
    s = ui -> expression -> text();
    ui -> expression -> setText(s+"3");
}


void MainWindow::on_b4_clicked()
{
    QString s;
    s = ui -> expression -> text();
    ui -> expression -> setText(s+"4");
}

void MainWindow::on_b5_clicked()
{
    QString s;
    s = ui -> expression -> text();
    ui -> expression -> setText(s+"5");
}

void MainWindow::on_b6_clicked()
{
    QString s;
    s = ui -> expression -> text();
    ui -> expression -> setText(s+"6");
}

void MainWindow::on_b7_clicked()
{
    QString s;
    s = ui -> expression -> text();
    ui -> expression -> setText(s+"7");
}

void MainWindow::on_b8_clicked()
{
    QString s;
    s = ui -> expression -> text();
    ui -> expression -> setText(s+"8");
}

void MainWindow::on_b9_clicked()
{
    QString s;
    s = ui -> expression -> text();
    ui -> expression -> setText(s+"9");
}

void MainWindow::on_b0_clicked()
{
    QString s;
    s = ui -> expression -> text();
    ui -> expression -> setText(s+"0");
}

void MainWindow::on_divide_clicked()
{
    QString s;
    s = ui -> expression -> text();
    if ((s.contains("+") || s.contains("-") || s.contains("*") || s.contains("/")) || !(s.contains("1") || s.contains("2") || s.contains("3") || s.contains("4") || s.contains("5") || s.contains("6") || s.contains("7") || s.contains("8") || s.contains("9") || s.contains("0"))) {
        ui -> expression -> setText(s);
    } else {
        ui -> expression -> setText(s+"/");
    }
}

void MainWindow::on_multiply_clicked()
{
    QString s;
    s = ui -> expression -> text();
    if ((s.contains("+") || s.contains("-") || s.contains("*") || s.contains("/")) || !(s.contains("1") || s.contains("2") || s.contains("3") || s.contains("4") || s.contains("5") || s.contains("6") || s.contains("7") || s.contains("8") || s.contains("9") || s.contains("0"))) {
        ui -> expression -> setText(s);
    } else {
        ui -> expression -> setText(s+"*");
    }
}

void MainWindow::on_minus_clicked()
{
    QString s;
    s = ui -> expression -> text();
    if ((s.contains("+") || s.contains("-") || s.contains("*") || s.contains("/")) || !(s.contains("1") || s.contains("2") || s.contains("3") || s.contains("4") || s.contains("5") || s.contains("6") || s.contains("7") || s.contains("8") || s.contains("9") || s.contains("0"))) {
        ui -> expression -> setText(s);
    } else {
        ui -> expression -> setText(s+"-");
    }
}

void MainWindow::on_plus_clicked()
{
    QString s;
    s = ui -> expression -> text();
    if ((s.contains("+") || s.contains("-") || s.contains("*") || s.contains("/")) || !(s.contains("1") || s.contains("2") || s.contains("3") || s.contains("4") || s.contains("5") || s.contains("6") || s.contains("7") || s.contains("8") || s.contains("9") || s.contains("0")) ) {
        ui -> expression -> setText(s);
    } else {
        ui -> expression -> setText(s+"+");
    }
}


void MainWindow::on_clear_clicked()
{
    ui -> expression -> setText("");
    ui -> result -> setText("");
}



void MainWindow::on_del_clicked()
{
    QString s;
    s = ui -> expression -> text();
    s.remove(s.length()-1, s.length());
    ui -> expression -> setText(s);
}



void MainWindow::on_x2_clicked()
{
    QString s;
    s = ui -> expression -> text();
    if ((s.contains("+") || s.contains("-") || s.contains("*") || s.contains("/")) || !(s.contains("1") || s.contains("2") || s.contains("3") || s.contains("4") || s.contains("5") || s.contains("6") || s.contains("7") || s.contains("8") || s.contains("9") || s.contains("0")) ) {
        ui -> expression -> setText(s);
    } else {
        double x = s.toDouble() * s.toDouble();
        s.setNum(x);
        ui -> result -> setText(s);
    }
}


void MainWindow::on_log_clicked()
{
    QString s;
    s = ui -> expression -> text();
    if ((s.contains("+") || s.contains("-") || s.contains("*") || s.contains("/")) || !(s.contains("1") || s.contains("2") || s.contains("3") || s.contains("4") || s.contains("5") || s.contains("6") || s.contains("7") || s.contains("8") || s.contains("9") || s.contains("0")) ) {
        ui -> expression -> setText(s);
    } else {
        double x = log(s.toDouble());
        s.setNum(x);
        ui -> result -> setText(s);
    }
}

void MainWindow::on_sin_clicked()
{
    QString s;
    s = ui -> expression -> text();
    if ((s.contains("+") || s.contains("-") || s.contains("*") || s.contains("/")) || !(s.contains("1") || s.contains("2") || s.contains("3") || s.contains("4") || s.contains("5") || s.contains("6") || s.contains("7") || s.contains("8") || s.contains("9") || s.contains("0")) ) {
        ui -> expression -> setText(s);
    } else {
        double x = sin(s.toDouble());
        s.setNum(x);
        ui -> result -> setText(s);
    }
}

void MainWindow::on_dB_clicked()
{
    QString s;
    s = ui -> expression -> text();
    if ((s.contains("+") || s.contains("-") || s.contains("*") || s.contains("/")) || !(s.contains("1") || s.contains("2") || s.contains("3") || s.contains("4") || s.contains("5") || s.contains("6") || s.contains("7") || s.contains("8") || s.contains("9") || s.contains("0")) ) {
        ui -> expression -> setText(s);
    } else {
        double x = 10 * log(s.toDouble()/0.001);
        s.setNum(x);
        ui -> result -> setText(s);
    }
}

void MainWindow::on_equals_clicked()
{
    QString s;
    s = ui -> expression -> text();
    if (s.contains("+")) {
        double x1, x2;
        QStringList l = s.split("+");
        x1 = l.first().toDouble();
        x2 = l.last().toDouble();
        ui->result->setText(s.setNum(x1+x2));
    }
    if (s.contains("-")) {
        double x1, x2;
        QStringList l = s.split("-");
        x1 = l.first().toDouble();
        x2 = l.last().toDouble();
        ui->result->setText(s.setNum(x1-x2));
    }
    if (s.contains("/")) {
        double x1, x2;
        QStringList l = s.split("/");
        x1 = l.first().toDouble();
        x2 = l.last().toDouble();
        if (x2 == 0) {
            ui->result->setText("Divided by zero");
        } else {
            ui->result->setText(s.setNum(x1/x2));
        }
    }
    if (s.contains("*")) {
        double x1, x2;
        QStringList l = s.split("*");
        x1 = l.first().toDouble();
        x2 = l.last().toDouble();
        ui->result->setText(s.setNum(x1*x2));
    }
}

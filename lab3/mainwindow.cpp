#include "mainwindow.h"
#include "ui_mainwindow.h"
#include <QProgressDialog>
#include <QMessageBox>
#include <QFont>
#include <QFontDialog>
#include <QColor>
#include <QColorDialog>

MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow)
{
    ui->setupUi(this);
}

MainWindow::~MainWindow()
{
    delete ui;
}

void MainWindow::on_pushButton_clicked()
{
    QMessageBox* pmbx = new QMessageBox("MessageBox", "<b>A</b><i>Simple</i><u>Message</u>", QMessageBox::Information, QMessageBox::Yes, QMessageBox::No, QMessageBox::Cancel | QMessageBox::Escape);
    pmbx->exec();
    delete pmbx;
}

void MainWindow::on_pushButton_2_clicked()
{
    int n = 10000000;
    QProgressDialog* pprd = new QProgressDialog("Progressing data...", "&Cancel", 0, n);
    pprd -> setMinimumDuration(0);
    pprd -> setWindowTitle("Wait a bit");
    for (int i = 0; i < n; i++) {
        pprd -> setValue(i);
        qApp -> processEvents();
        if(pprd -> wasCanceled()) {
            break;
        }
    }
    pprd -> setValue(n);
    delete pprd;
}

void MainWindow::on_pushButton_3_clicked()
{
    QColor c = QColorDialog::getColor();
    if (!c.isValid()) {
        return;
    } else {
        QPalette palette = qApp->palette();
        palette.setColor(QPalette::Background, c);
        qApp->setPalette(palette);
    }
}

void MainWindow::on_pushButton_4_clicked()
{
    bool ok;
    QFont font = QFontDialog::getFont(&ok, QFont("Helvetica [Cronyx]", 10), this);
    if (ok) {
        QApplication::setFont(font);
    } else {
        QApplication::setFont(QFont("Helvetica [Cronyx]", 10));
    }
}

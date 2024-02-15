#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>

namespace Ui {
class MainWindow;
}

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    explicit MainWindow(QWidget *parent = 0);
    ~MainWindow();

private slots:
    void on_plus_clicked();

    void on_multy_clicked();

    void on_divide_clicked();

    void on_sin_1_clicked();

    void on_sin_2_clicked();

    void on_pow_1_clicked();

    void on_pow_2_clicked();

    void on_minus_clicked();

    void on_sqrt_1_clicked();

    void on_sqrt_2_clicked();

    void on_log_1_clicked();

    void on_log_2_clicked();

private:
    Ui::MainWindow *ui;
};

#endif // MAINWINDOW_H

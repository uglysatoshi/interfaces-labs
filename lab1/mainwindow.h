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
    void on_b1_clicked();

    void on_b2_clicked();

    void on_b3_clicked();

    void on_b4_clicked();

    void on_b5_clicked();

    void on_b6_clicked();

    void on_b7_clicked();

    void on_b8_clicked();

    void on_b9_clicked();

    void on_b0_clicked();

    void on_divide_clicked();

    void on_multiply_clicked();

    void on_minus_clicked();

    void on_plus_clicked();

    void on_clear_clicked();

    void on_del_clicked();

    void on_x2_clicked();

    void on_log_clicked();

    void on_sin_clicked();

    void on_dB_clicked();

    void on_equals_clicked();

private:
    Ui::MainWindow *ui;
};

#endif // MAINWINDOW_H

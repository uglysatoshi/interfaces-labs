#include "mainwindow.h"
#include "ui_mainwindow.h"

MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow)
{
    ui->setupUi(this);
    ui->pushButton->setToolTip("Подсказка<BR><B>ПАСХАЛОЧКА</B>");
    QMenu* menu = new QMenu("&Menu");
    menu->addAction("&About Qt", parent, SLOT(aboutQt()), Qt::CTRL+Qt::Key_Q);
    menu->addSeparator();
    menu->addAction("&CheckableItem");
    QMenu* pmnuSubMenu = new QMenu("&SubMenu", menu);
    pmnuSubMenu->addAction("&Test");
    menu->addMenu(pmnuSubMenu);
    QAction* pDisableAction = menu->addAction("&DisableItem");
    pDisableAction->setEnabled(false);
    menu->addSeparator();
    menu->addAction("&Exit", parent, SLOT(quit()));
    menu->setTearOffEnabled(true);
    ui->menuBar->addMenu(menu);

}

MainWindow::~MainWindow()
{
    delete ui;
}

void MainWindow::on_pushButton_clicked()
{
    ui->statusBar->showMessage("Message!!", 0);
}

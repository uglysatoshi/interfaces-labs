#include "mainwindow.h"
#include <QApplication>
#include <QMenuBar>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    MainWindow w;
    w.show();

    QMenu* menu = new QMenu("&Menu");
    menu->addAction("&About Qt", &a, SLOT(aboutQt()), Qt::CTRL+Qt::Key_Q);
    menu->addSeparator();
    menu->addAction("&CheckableItem");
    QMenu* pmnuSubMenu = new QMenu("&SubMenu", menu);
    pmnuSubMenu->addAction("&Test");
    menu->addMenu(pmnuSubMenu);
    QAction* pDisableAction = menu->addAction("&DisableItem");
    pDisableAction->setEnabled(false);
    menu->addSeparator();
    menu->addAction("&Exit", &a, SLOT(quit()));
    menu->setTearOffEnabled(true);
    w.menuBar()->addMenu(menu);

    return a.exec();

}

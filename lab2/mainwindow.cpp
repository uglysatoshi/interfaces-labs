#include "mainwindow.h"
#include "ui_mainwindow.h"
#include <QMessageBox>

MainWindow::MainWindow(QWidget *parent) : QMainWindow(parent), ui(new Ui::MainWindow) {
    ui -> setupUi(this);
    m_db = QSqlDatabase::addDatabase("QSQLITE");
    m_db.setDatabaseName("Petrovich");
    query = new QSqlQuery(m_db);
    m_db.open();
    if(!m_db.open())
        throw "can't open database";
    if(!m_db.tables().contains("Person")){
        query->clear();
        query->exec("CREATE Table Petrovich(ID INTEGER PRIMARY KEY, Item VARCHAR, Type VARCHAR, Amount INTEGER);");
        query->clear();
        query->exec("INSERT INTO Petrovich(ID,Item,Type,Amount) VALUES (1,'Помидоры', 'Овощи', 53);");
        query->clear();
        query->exec("INSERT INTO Petrovich(ID,Item,Type,Amount) VALUES (2,'Баклажаны', 'Овощи', 52);");
        query->clear();
        query->exec("INSERT INTO Petrovich(ID,Item,Type,Amount) VALUES (3,'Арбузы', 'Ягоды', 30);");
    }
    model = new QSqlTableModel(this,m_db);
    model->setTable("Petrovich");
    model->select();
    model->setEditStrategy(QSqlTableModel::OnFieldChange);
    ui->tableView->setModel(model);
}

MainWindow::~MainWindow() {
    delete ui;
    delete query;
    delete model;
}

void MainWindow::on_pushButton_clicked()
{
    model->setFilter("Amount<50");
    model->select();
    ui->tableView->setModel(model);
}

void MainWindow::on_pushButton_2_clicked()
{
    model->setFilter("");
    model->select();
    ui->tableView->setModel(model);
}

void MainWindow::on_pushButton_3_clicked()
{
    model->setFilter("Amount>50");
    model->select();
    ui->tableView->setModel(model);
}

void MainWindow::on_pushButton_4_clicked()
{
    if (ui->Item->text().isEmpty() || ui->Amout->text().isEmpty() || ui->Type->text().isEmpty()|| ui->ID->text().isEmpty()){
        return;
    } else {
        query->clear();
        QString id = ui->ID->text();
        QString item = ui->Item->text();
        QString amout = ui->Amout->text();
        QString type = ui->Type->text();
        QString buf = tr("INSERT INTO Petrovich (ID,Item,Type,Amount) VALUES (")+id+tr(",'")+item+tr("','")+type+tr("',")+amout+tr(");");
        query->exec(buf);
        model->select();
    }
}

void MainWindow::on_horizontalSlider_valueChanged(int value)
{
    model->setFilter(QString("Amount>%1").arg(value));
    model->select();
    ui->tableView->setModel(model);
}

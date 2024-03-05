#include "mainwindow.h"
#include "ui_mainwindow.h"
#include <QMessageBox>

MainWindow::MainWindow(QWidget *parent) : QMainWindow(parent), ui(new Ui::MainWindow)
{
    ui->setupUi(this);
    m_db = QSqlDatabase::addDatabase("QSQLITE");
    m_db.setDatabaseName("myDB");
    query = new QSqlQuery(m_db);
    if(!m_db.open())
        throw "can't open database";
    if(!m_db.tables().contains("Person")) {
        query->clear();
        query->exec("CREATE TABLE Person(ID INTEGER PRIMARY KEY, Name VARCHAR, Year INTEGER);");
        query->clear();
        query->exec("INSERT INTO Person (ID,Name,Year) VALUES (1,'Ann', 2000);");
        query->clear();
        query->exec("INSERT INTO Person (ID,Name,Year) VALUES (2,'Jim', 2003);");
    }
    model = new QSqlTableModel(this,m_db);
    model->setTable("Person");
    model->select();
    model->setEditStrategy(QSqlTableModel::OnFieldChange);
    ui->tableView->setModel(model);
}

MainWindow::~MainWindow()
{
    delete ui;
    delete query;
    delete model;
}

#ifndef GLWIDGET_H
#define GLWIDGET_H
#include <QGLWidget>
#include <cmath>

class GLWidget : public QGLWidget
{
Q_OBJECT
public:
explicit GLWidget(QWidget *parent = 0); void initializeGL();
void paintGL();
void resizeGL(int w,int h);

public:
static int curvature;

static int rotateX,rotateY,angle; float func(float, float);
public slots:
void ChangeStructFunc(int); void ChangeX(int);
void ChangeY(int); void ChangeAngle(int);

};
#endif // GLWIDGET_H

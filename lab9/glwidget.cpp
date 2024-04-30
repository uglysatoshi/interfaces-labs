#include "glwidget.h"
#include <QDebug>

int GLWidget::curvature=0;
int GLWidget::rotateX=0;
int GLWidget::rotateY=0;
int GLWidget::angle=45;
void GLWidget::ChangeStructFunc(int slValue){
    curvature=slValue;
    updateGL();
}
void GLWidget::ChangeX(int slValue){
    rotateX=slValue;
    updateGL();
}
void GLWidget::ChangeY(int slValue){
    rotateY=slValue;
    updateGL();
}
void GLWidget::ChangeAngle(int slValue){
    angle=slValue;
    updateGL();
}
GLWidget::GLWidget(QWidget *parent):QGLWidget(parent)
{

}
void GLWidget::initializeGL(){
    glClearColor(0,0,0,1);
    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    glFrustum(-100, 100, -100, 100, 100, 2000);
    glMatrixMode(GL_MODELVIEW);
    glLoadIdentity();
}
void GLWidget::paintGL(){
    glClear(GL_COLOR_BUFFER_BIT);
    glPushMatrix();
    glTranslatef(0,0, -800);
    glRotatef(angle,rotateX, rotateY,45);
    glColor3f(1,1,0);
    double wScale=1;
    int StepGrid=20;
    for(float x = -480; x<480; x+=StepGrid){
        glBegin(GL_LINE_STRIP);
        for(float y = -480; y<480; y+=StepGrid){
            glVertex3f(x*wScale,y*wScale, func(x*wScale,y*wScale));

        }
        glEnd();
    }
   for(float y = -480; y<480; y+=StepGrid){
       glBegin(GL_LINE_STRIP);
       for(float x = -480; x<480; x+=StepGrid){
           glVertex3f(x*wScale, y*wScale,func(x*wScale,y*wScale));

       }
       glEnd();
   }
   glPopMatrix();
}
void GLWidget::resizeGL(int w, int h){
    glViewport(0,0,(GLint)w,(GLint)h);
}
float GLWidget::func(float x, float y){
    return tan(x*y*0.0001)*curvature;
}



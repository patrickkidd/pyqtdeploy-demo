#include <QDebug>
#include "_cpythonplusqt.h"

SomePushButton::SomePushButton(QWidget *parent) : 
QPushButton(parent)
{
}

void SomePushButton::mousePressEvent(QMouseEvent *e) {
    qInfo() << e;
}

void SomePushButton::mouseReleaseEvent(QMouseEvent *e) {
    qInfo() << e;
}

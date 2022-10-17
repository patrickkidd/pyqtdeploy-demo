#include <QtWidgets>


class SomePushButton : public QPushButton {

Q_OBJECT

public:
    SomePushButton(QWidget *parent);

    virtual void mousePressEvent(QMouseEvent *);
    virtual void mouseReleaseEvent(QMouseEvent *);
};
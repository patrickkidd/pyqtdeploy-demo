%Module _cpythonplusqt
%Import QtCore/QtCoremod.sip
%Import QtGui/QtGuimod.sip
%Import QtWidgets/QtWidgetsmod.sip


%ModuleHeaderCode
#include <_cpythonplusqt.h>
%End


class SomePushButton : public QPushButton {
    
public:
	SomePushButton(QWidget *parent);
//    ~SomePushButton();
};

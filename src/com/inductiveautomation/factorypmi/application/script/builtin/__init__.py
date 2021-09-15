__all__ = ["INavUtilities", "PrintUtilities"]

from abc import ABCMeta, abstractmethod

from java.awt.image import BufferedImage
from java.lang import Object


class INavUtilities(ABCMeta):
    """Parent interface to coordinate the functions between NavUtilities
    and NavUtilitiesDispatcher.
    """

    def __new__(mcs, *args, **kwargs):
        pass

    @abstractmethod
    def centerWindow(cls, arg):
        pass

    @abstractmethod
    def closeParentWindow(cls, event):
        pass

    @abstractmethod
    def closeWindow(cls, arg):
        pass

    @abstractmethod
    def getCurrentWindow(cls):
        pass

    @abstractmethod
    def goBack(cls):
        pass

    @abstractmethod
    def goForward(cls):
        pass

    @abstractmethod
    def goHome(cls):
        pass

    @abstractmethod
    def openWindow(cls, path, params=None):
        pass

    @abstractmethod
    def openWindowImpl(cls, path, params, openAdditional):
        pass

    @abstractmethod
    def openWindowInstance(cls, path, params=None):
        pass

    @abstractmethod
    def swapTo(cls, path, params=None):
        pass

    @abstractmethod
    def swapWindow(cls, *args):
        pass


class PrintUtilities(Object):
    def __init__(self, app):
        self.app = app

    def createImage(self, c):
        print(self, c)
        width = height = imageType = 1
        return BufferedImage(width, height, imageType)

    def createPrintJob(self, c):
        pass

    def printToImage(self, c, fileName=None):
        pass

    class JythonPrintJob(Object):
        def getBottomMargin(self):
            pass

        def getLeftMargin(self):
            pass

        def getOrientation(self):
            pass

        def getPageHeight(self):
            pass

        def getPageWidth(self):
            pass

        def getPrinterName(self):
            pass

        def getRightMargin(self):
            pass

        def getTopMargin(self):
            pass

        def getZoomFactor(self):
            pass

        def isFitToPage(self):
            pass

        def isShowPrintDialog(self):
            pass

        def setBottomMargin(self, bottomMargin):
            pass

        def setFitToPage(self, fitToPage):
            pass

        def setLeftMargin(self, leftMargin):
            pass

        def setMargins(self, m):
            pass

        def setOrientation(self, orientation):
            pass

        def setPageHeight(self, pageHeight):
            pass

        def setPageWidth(self, pageWidth):
            pass

        def setPrinterName(self, printerName):
            pass

        def setRightMargin(self, rightMargin):
            pass

        def setShowPrintDialog(self, showPrintDialog):
            pass

        def setZoomFactor(self, zoomFactor):
            pass

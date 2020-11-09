from gui.main_window import MainWindow
import extractor


if __name__ == '__main__':
    app = MainWindow(extractor.do_processing)
    app.run()
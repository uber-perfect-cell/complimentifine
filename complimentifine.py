from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt

def rgbConvert(colour):
    colour = colour.lstrip('#')
    colours = [] 
    for i in (0,2,4):
        hex = colour[i:i+2]
        rgb = int(hex, 16)
        colours.append(rgb)
    print(tuple(colours))
    return tuple(colours)

def complimentifine(rgbv):
    compliment = tuple(255 - component for component in rgbv)
    return compliment

def hexConvert(complimentified):
    r, g, b = complimentified
    return "#{:02x}{:02x}{:02x}".format(r,g,b)

def finishingTouches(sc, selectedColourLabel, complementColourLabel, selectedColourTextLabel, selectedComplimentTextLabel):
    rgbv = rgbConvert(sc)  
    complimentified = complimentifine(rgbv)
    complementairyColour = hexConvert(complimentified)
    print(complementairyColour)
    selectedColourLabel.setStyleSheet(f"background-color: {sc};")
    complementColourLabel.setStyleSheet(f"background-color: {complementairyColour}; ")
    selectedColourTextLabel.setText(f"Your chosen colour: {sc}")
    selectedComplimentTextLabel.setText(f"Your complimentary colour: {complementairyColour}")

def main(): 
    app = QApplication([])
    window = QWidget()

    selectedColourLabel = QLabel(window)
    selectedColourLabel.setFixedSize(300, 100)
    
    complementColourLabel = QLabel(window)
    complementColourLabel.setFixedSize(300, 100)

    selectedColourTextLabel = QLabel(window)
    selectedComplimentTextLabel = QLabel(window)
     
    selectedColourTextLabel.setFont(QFont('Fiery-Code', 16))
    selectedComplimentTextLabel.setFont(QFont('Fiery-Code', 16))
    selectedComplimentTextLabel.setAlignment(Qt.AlignCenter)
    selectedColourTextLabel.setAlignment(Qt.AlignCenter)
    
    button = QPushButton("Open Colour Wheel")
    button.clicked.connect(lambda: openColourWheel(selectedColourLabel, complementColourLabel, selectedColourTextLabel, selectedComplimentTextLabel))

    window.setWindowTitle('Complimentifine')

    colorLayout = QHBoxLayout()
    colorLayout.addStretch(1)
    colorLayout.addWidget(selectedColourLabel)
    colorLayout.addWidget(complementColourLabel)
    colorLayout.addStretch(1)
    
    layout = QVBoxLayout()
    layout.addLayout(colorLayout)
    layout.addWidget(selectedColourTextLabel)
    layout.addWidget(selectedComplimentTextLabel)
    layout.addWidget(button)

    window.setLayout(layout)
    window.show()
    app.exec()


def openColourWheel(selectedColourLabel, complementColourLabel, selectedColourTextLabel, selectedComplimentTextLabel):
    selectedColour = QColorDialog.getColor()
    if selectedColour.isValid():
        print(f"Selected colour: {selectedColour.name()}")
        finishingTouches(selectedColour.name(), selectedColourLabel, complementColourLabel, selectedColourTextLabel, selectedComplimentTextLabel)
    
if __name__ == '__main__':
    main()


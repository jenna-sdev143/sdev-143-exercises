# making a basic pyqt app
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QScrollArea, QLineEdit, QPushButton, QTextEdit
from PyQt5.QtGui import QFont, QColor
from PyQt5.QtCore import Qt

# class for the window 
class GitCommandApp(QWidget):
    def __init__(self):
        super().__init__()

        # basic window set up
        self.setWindowTitle("Git Terminal Simulator")
        self.setGeometry(200, 200, 600, 500) # x, y, width, height 
        
        # set style to look like terminal
        self.setStyleSheet("background-color: black; color: #00ff00")

        # set custom font
        font = QFont("Courier", 10)
        font.setStyleHint(QFont.Monospace)

        # styled text for common git commands
        text = """
        <b>Common Git Commands</b><br><br>
        <code><span style="color: #ff4500;">git init</span></code> - Initializes a Git repository.<br>
        <code><span style="color: #ff4500;">git clone &lt;repo-url&gt;</span></code> - Copies a remote repo.<br>
        <code><span style="color: #ff4500;">git add &lt;file&gt;</span></code> - Stages changes.<br>
        <code><span style="color: #ff4500;">git commit -m "message"</span></code> - Saves changes.<br>
        <code><span style="color: #ff4500;">git push</span></code> - Uploads changes to remote repo.<br>
        """

        # label - putting txt in there instead
        label = QLabel(text)
        # word wrap
        label.setWordWrap(True)
        # set font
        label.setFont(font)
        label.setStyleSheet("color: #ffffff;") # white text 

        # scroll area instead
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True) # allows for resizing
        scroll_area.setWidget(label) # put my text inside the scroll area

        # input field (styled to look like terminal input)
        self.input_field = QLineEdit()
        self.input_field.setPlaceholderText("Enter a Git command...")
        self.input_field.setStyleSheet(
            "background-color: black; color: #00ff00; border: 1px solid #00ff00; padding: 5px;"
        )
        self.input_field.setFont(font)

        # styled button to run command
        run_btn = QPushButton("Run Command")
        run_btn.setStyleSheet(
            "backgrounf-color: #333333; color: #00ff00; border: 1px solid #00ff00; padding: 5px;"
        )
        run_btn.clicked.connect(self.fake_git_output)

        # styled output box
        self.output_box = QTextEdit()
        self.output_box.setReadOnly(True) # cant edit the txt box only read
        self.output_box.setFont(font)
        self.output_box.setStyleSheet(
            "background-color: #333333; color: #00ff00; border: 1px solid #00ff00; padding: 5px;"
        )

        # layout
        layout = QVBoxLayout()
        layout.addWidget(scroll_area) # add scroll area to layout
        layout.addWidget(self.input_field)
        layout.addWidget(run_btn)
        layout.addWidget(self.output_box)

        # set the layout
        self.setLayout(layout)

    # making a function that simulates git command output
    def fake_git_output(self):
        """Simulates git command output"""
        command = self.input_field.text().strip()

        # dictionary of fake git responses
        git_responses = {
            "git init": "Initialized empty Git repository in /your/project/path/.git/",
            "git clone <repo-url>": "Cloning into 'repo-name'...\nremote: Enumerating objects: 100, done.",
            "git add <file>": "File added to staging area.",
            "git commit -m \"message\"": "[main 123abc] message\n 1 file changed, 1 insertion(+)",
            "git push": "Counting objects: 5, done.\nTo github.com:user/repo.git\n * [new branch] main -> main",
            "git pull": "Already up to date.",
            "git status": "On branch main\nYour branch is up to date with 'origin/main'.\nNothing to commit, working tree clean.",
            "git log": "commit 123abc (HEAD -> main)\nAuthor: You <you@example.com>\nDate: Today\n\n    Initial commit",
            "git branch": "* main",
        }

        # get fake output or show error msg
        output = git_responses.get(command, "Error: Unknown command")

        # formatted output display
        self.output_box.append(f"{command}\b{output}\n")
   

# main func to run app
def main():
    app = QApplication(sys.argv)
    window = GitCommandApp()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
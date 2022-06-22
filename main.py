import streamlit as st
from streamlit import cli as stcli
import sys
from pathlib import Path
from os.path import dirname, join

st.set_page_config(layout="wide")


class App:
    """Class to build a streamlit web app"""
    def __init__(self):
        pass

    @staticmethod
    def format_title() -> None:
        """Display title of the app at screen."""
        col_im_left, col_title = st.columns([1, 2])
        with col_im_left:
            st.image(join(Path(dirname(__file__)), 'streamlit-mark-light.png'), width=200)
        with col_title:
            st.markdown("# Streamlit Web Application")

    def show(self):
        self.format_title()


def main():
    front = App()
    front.show()


if __name__ == '__main__':
    if st._is_running_with_streamlit:
        main()
    else:
        sys.argv = ["streamlit", "run", sys.argv[0]]
        sys.exit(stcli.main())
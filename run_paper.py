import os
import shutil
from subprocess import call, CalledProcessError
import glob

def clean_directories(base_path):
    print("Cleaning Output and Temporary directories")
    for folder in ['/output', '/tmp']:
        folder_path = os.path.join(base_path, folder.strip('/'))
        if os.path.exists(folder_path):
            shutil.rmtree(folder_path)
        try:
            os.makedirs(folder_path, exist_ok=True)
            print(f"Created directory: {folder_path}")
        except Exception as e:
            print(f"Error creating directory {folder_path}: {e}")
    print("Directories cleaned")

def get_input(base_path):
    print("Getting Input")
    call(['python', os.path.join(base_path, 'code/get_input.py')])
    print("Input obtained")

def run_build(base_path):
    print("Running Build")
    call(['python', os.path.join(base_path, 'code/build.py')])  # Make sure this script exists
    for file in glob.glob(os.path.join(base_path, 'output/logs/*.log')):
        os.remove(file)
    print("Build executed")

def run_analysis(base_path):
    print("Running Analysis")
    call(['python', os.path.join(base_path, 'code/analysis.py')])  # Make sure this script exists
    for file in glob.glob(os.path.join(base_path, 'output/logs/*.log')):
        os.remove(file)
    print("Analysis executed")

def compile_tex(base_path):
    print("Compiling TeX")
    tex_file = os.path.join(base_path, 'products/paper/main_article.tex')
    if not os.path.isfile(tex_file):
        print(f"Error: TeX file not found at {tex_file}")
        return

    try:
        call(['latexmk', tex_file])
        print("TeX compiled")
    except CalledProcessError as e:
        print(f"Error compiling TeX: {e}")
    except FileNotFoundError:
        print("Error: latexmk command not found. Make sure LaTeX is installed and latexmk is available in your PATH.")

def main():
    base_path = '/path/to/main_paper'  # Update this to your actual path
    clean_directories(base_path)
    get_input(base_path)
    run_build(base_path)
    run_analysis(base_path)
    compile_tex(base_path)
    print("Congratulations, you have a shiny new paper!")

if __name__ == "__main__":
    main()

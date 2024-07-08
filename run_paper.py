import os
import shutil
from subprocess import call, CalledProcessError, run, PIPE
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
    pdf_file = os.path.join(base_path, 'products/paper/main_article.pdf')

    if not os.path.isfile(tex_file):
        print(f"Error: TeX file not found at {tex_file}")
        return False, "TeX file not found"

    try:
        result = run(['latexmk', '-pdf', tex_file], stdout=PIPE, stderr=PIPE, text=True)
        if result.returncode != 0:
            print(f"Error compiling TeX: {result.stderr}")
            return False, result.stderr
        if os.path.isfile(pdf_file):
            return pdf_file, "TeX compiled successfully"
        else:
            print("Error: PDF file not generated")
            return False, "PDF file not generated"
    except CalledProcessError as e:
        print(f"Error compiling TeX: {e}")
        return False, str(e)
    except FileNotFoundError:
        print("Error: latexmk command not found. Make sure LaTeX is installed and latexmk is available in your PATH.")
        return False, "latexmk command not found"

def main():
    base_path = '/path/to/main_paper'  # Update this to your actual path
    clean_directories(base_path)
    get_input(base_path)
    run_build(base_path)
    run_analysis(base_path)
    pdf_file, message = compile_tex(base_path)
    if pdf_file:
        print("Congratulations, you have a shiny new paper!")
    else:
        print(f"Compilation failed: {message}")

if __name__ == "__main__":
    main()

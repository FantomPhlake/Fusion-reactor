#This is the homepage of the website

print("Welcome to the world's first (maybe) online fusion reactor prototype")
print("We humans have been working on nuclear fusion for the past 10 years (30 actually) so i decided to create an online nuclear reactor prototype")
print("Before heading right to it we have to get you summarized with nuclear fusion and reactor mechanics:")

#This redirects the user into a popup if the user selects "let's go!"

from flask import Flask, render_template_string, request

app = Flask(__name__)

HTML_TEMPLATE = '''
<!DOCTYPE html>
<html>
<head>
  <style>
    .modal {
      display: {{ 'block' if show_modal else 'none' }};
      position: fixed;
      z-index: 1000;
      top: 0; left: 0;
      width: 100%; height: 100%;
      background-color: rgba(0, 0, 0, 0.8);
      overflow: auto;
    }
    .modal-content {
      background-color: #000;
      color: white;
      margin: 15% auto;
      padding: 20px;
      width: 40%;
      border-radius: 8px;
      box-shadow: 0 0 10px white;
      position: relative;
    }
    .close {
      position: absolute;
      top: 10px; right: 15px;
      font-size: 28px;
      font-weight: bold;
      color: white;
      cursor: pointer;
    }
    .close:hover {
      color: #bbb;
    }
    button {
      font-size: 18px;
      padding: 10px 30px;
      cursor: pointer;
    }
  </style>
  <script>
    function closeModal() {
      document.getElementById("myModal").style.display = "none";
    }
    window.onclick = function(event) {
      var modal = document.getElementById("myModal");
      if(event.target == modal) {
        modal.style.display = "none";
      }
    }
  </script>
</head>
<body>

  <form method="post">
    <button type="submit" name="choice" value="lets_go">Let's go!</button>
  </form>

  <div id="myModal" class="modal">
    <div class="modal-content">
      <span class="close" onclick="closeModal()">&times;</span>
      <h2>Introduction</h2>
      <p>Welcome!</p>
      <p>Please read everything carefully and proceed when ready:</p>
      <p>So first of all let me tell you something about the most basic nuclear fusion that occurs at the sun's core.</p>
      <p>At the sun's core, which is really hot by the way (about 15 million degrees Celsius), hydrogen atoms come together to fuse into Helium 4.</p>
      <p>You thought that's it? Let me make it more concrete</p>
      <p>So, two protium (normal hydrogen) atoms undergo through a series of reactions by the proton-proton chain (p-p) and they break the Coloumbic barrier to form deuterium (isotope of hydrogen with twice the mass number) through quantum tunneling.</p>
      <p>As there are many hydrogen-hydrogen fusions occuring, further these deuterium atoms also fuse with protons to create helium-3 and helium-3 fusing with another proton to create helium-4.</p>
      <p>Let's get straight to the point right now, these series of reactions cumulatively keeps the core hot and powers the entire sun.</p>
      <p>Yes, this massive energy can be used to power up literally everything thanks to electric lines and grids.</p>
    </div>
  </div>

</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def index():
    show_modal = False
    if request.method == 'POST':
        choice = request.form.get('choice')
        if choice == 'lets_go':
            show_modal = True  # Shows the modal on button click
    return render_template_string(HTML_TEMPLATE, show_modal=show_modal)

if __name__ == '__main__':
    app.run(debug=False)



import os
from os.path import join, dirname
from dotenv import load_dotenv
from flask import Flask, render_template, request, jsonify, escape
from pymongo import MongoClient

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

MONGODB_URL = os.environ.get("MONGODB_URL")
DBNAME = os.environ.get("DB_NAME")

client = MongoClient(MONGODB_URL)
app = Flask(__name__)

db = client[DBNAME]

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/mars", methods=["POST"])
def web_mars_post():
    name_receive = escape(request.form['name_give'])
    address_receive = escape(request.form['address_give'])
    size_receive = escape(request.form['size_give'])
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <meta name="theme-color" content="#3498db">
    <link rel='website icon' type="png" href="https://j.top4top.io/p_2676j87ku1.png">

    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous" />
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM" crossorigin="anonymous"></script>

    <link href="https://fonts.googleapis.com/css2?family=Gowun+Batang:wght@400;700&display=swap" rel="stylesheet" />

    <title>Mars Land Purchase Site</title>
    
    <style>
          * {
        font-family: "Gowun Batang", serif;
        color: white;
      }

      body {
        background-image: linear-gradient(0deg, rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5)), url("https://cdn.aitimes.com/news/photo/202010/132592_129694_3139.jpg");
        background-position: center;
        background-size: cover;
      }

      h1 {
        font-weight: bold;
      }

      .order {
        width: 500px;
        margin: 60px auto 0px auto;
        padding-bottom: 60px;
      }

      .mybtn {
        width: 100%;
      }

      .order > table {
        margin: 40px 0;
        font-size: 18px;
      }

      option {
        color: black;
      }
      
      /* Footer */
    footer {
      background-color: #1a1a1a;
      color: #fff;
      padding: 50px 0;
    }

    .footer-box {
      margin-bottom: 30px;
    }

    .footer-text {
      margin-top: 15px;
    }

    .footer-heading {
      font-size: 24px;
      margin-bottom: 30px;
    }

    .footer-list {
      list-style: none;
      margin: 0;
      padding: 0;
    }

    .footer-list li {
      margin-bottom: 10px;
    }

    .footer-list a {
      color: #fff;
    }

    .footer-list a:hover {
      color: #f1c40f;
    }

    .fa {
      margin-right: 10px;
    }

    hr {
      border-color: #fff;
      margin-top: 50px;
      margin-bottom: 50px;
    }

    </style>
    
    <script>
      $(document).ready(function () {
        show_order();
      });

      function show_order() {
        $.ajax({
          type: "GET",
          url: "/mars",
          data: {},
          success: (response) => {
            let orders = response["orders"];
            orders.forEach((order) => {
              let name = order["name"];
              let address = order["address"];
              let size = order["size"];

              let temp_html = `
                <tr>  
                  <td>${name}</td> 
                  <td>${address}</td> 
                  <td>${size}</td>
                </tr>`;

              $("#orders_box").append(temp_html);
            });
          },
        });
      }

      function save_order() {
        let name = $("#name").val();
        let address = $("#address").val();
        let size = $("#size").val();
        $.ajax({
          type: "POST",
          url: "/mars",
          data: {
            name_give: name,
            address_give: address,
            size_give: size,
          },
          success: function (response) {
            alert(response["msg"]);
            window.location.reload();
          },
        });
      }
    </script>
  </head>

  <body>
        <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
      <div class="container-fluid">
        <a class="navbar-brand" href="http://profesords.rf.gd/">Profesords</a>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNav">
          <ul class="navbar-nav">
            <li class="nav-item">
              <a class="nav-link" href="#">Home</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="http://profesords.rf.gd#about">About</a>
            </li>
            <li class="nav-item dropdown">
              <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-bs-toggle="dropdown" aria-expanded="false"> Project </a>
              <ul class="dropdown-menu" aria-labelledby="navbarDropdown">
                <li><a class="dropdown-item" href="https://sayoga-funbook.glitch.me/">FunBook</a></li>
                <li><a class="dropdown-item active" href="">Buy Martian Land</a></li>
                <li><a class="dropdown-item" href="https://sayoga-bucket-list.glitch.me">Bucket List</a></li>
                <li><a class="dropdown-item" href="https://sayoga-spartapedia.glitch.me/">Spartapedia</a></li>
              </ul>
            </li>
          </ul>
        </div>
      </div>
    </nav>
    <div class="mask"></div>
    <div class="order">
      <h1>Buy Martian Land!</h1>
      <h3>Price: $1.00 / acre</h3>
      <p>
        Did you know you could buy Martian land?<br />
        This chance won't come again!
      </p>
      <div class="order-info">
        <div class="input-group mb-3">
          <span class="input-group-text">Name</span>
          <input id="name" type="text" class="form-control" />
        </div>
        <div class="input-group mb-3">
          <span class="input-group-text">Address</span>
          <input id="address" type="text" class="form-control" />
        </div>
        <div class="input-group mb-3">
          <label class="input-group-text" for="size">Acres</label>
          <select class="form-select" id="size">
            <option selected>-- Select acreage --</option>
            <option value="10">10 acres</option>
            <option value="20">20 acres</option>
            <option value="30">30 acres</option>
            <option value="40">40 acres</option>
            <option value="50">50 acres</option>
          </select>
        </div>
        <button onclick="save_order()" type="button" class="btn btn-warning mybtn">Create order</button>
      </div>
      <table class="table">
        <thead>
          <tr>
            <th scope="col">Name</th>
            <th scope="col">Address</th>
            <th scope="col">Acres</th>
          </tr>
        </thead>
        <tbody id="orders_box"></tbody>
      </table>
    </div>
    
<footer>
  <div class="container">
    <div class="row">
      <div class="col-md-4 col-sm-6 footer-box">
        <img src="https://d.top4top.io/p_2673v44fh1.png" width="50" alt="Logo">
        <p class="footer-text">Security System Alert adalah sebuah komunitas berbasis cyber security yang mengedepankan kehati-hatian dan kewaspadaan seperti burung hantu, untuk melindungi sistem keamanan informasi.</p>
      </div>
      <div class="col-md-4 col-sm-6 footer-box">
        <h3 class="footer-heading">Quick Links</h3>
        <ul class="footer-list">
          <li><a href="http://profesords.rf.gd">My Website</a></li>
          <li><a href="http://profesords.rf.gd/#about">About</a></li>
          <li><a href="#">Services</a></li>
          <li><a href="http://profesords.rf.gd/#contact">Contact</a></li>
        </ul>
      </div>
      <div class="col-md-4 col-sm-12 footer-box">
        <h3 class="footer-heading">Contact Us</h3>
        <ul class="footer-list">
          <li><i class="fa fa-map-marker"></i> 15413 Ciputat, Tangerang Selatan </li>
          <li><i class="fa fa-phone"></i> +62 858 1401 5797</li>
          <li><i class="fa fa-envelope"></i> info@profesords.rf.gd</li>
        </ul>
      </div>
    </div>
    <div class="row">
      <div class="col-md-12">
        <hr>
        <p class="footer-text">&copy; 2023 SayogaPratama. All Rights Reserved.</p>
      </div>
    </div>
  </div>
</footer>


  </body>
</html>

    doc = {
        'name': name_receive,
        'address': address_receive,
        'size': size_receive
    }

    db.orders.insert_one(doc)
    return jsonify({'msg': 'complete'})


@app.route("/mars", methods=["GET"])
def mars_get():
    orders_list = list(db.orders.find({},{'_id':False}))
    return jsonify({'orders':orders_list})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
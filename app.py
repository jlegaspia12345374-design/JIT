from flask import Flask, render_template_string, request, redirect, url_for

app = Flask(__name__)

# CSS style
style_css = """
body { background-color: black; }
h1 { color: white; }
h2 { color: white; }
h3 { color: white; }
label { color: white; }

button {
    border-style: solid;
    border-width: 5px;
    border-color: grey;
    border-radius: 10px;
    padding: 5px;
    width: 200px;
    height: 60px;
    font-size: 20px;
}
"""

# Initial page
initial_html = """
<html>
<head>
    <title>Initial page</title>
    <style>{{ style }}</style>
</head>
<body>
    <center>
        <h1><b>JUNGLE GYM</b></h1>
        <hr>
        <br>
        <div><a href="{{ url_for('login') }}"><button style="background-color:black;color:red">Click here to login or register</button></a></div>
        <br>
        <div><a href="{{ url_for('info') }}"><button style="background-color:black;color:green">Click here to learn more about us</button></a></div>
        <br>
        <div><a href="{{ url_for('members') }}"><button style="background-color:black;color:blue">Click here to see our members</button></a></div>
        <br>
    </center>
</body>
</html>
"""

# Info page
info_html = """
<html>
<head>
    <title>INFO</title>
    <style>{{ style }}</style>
</head>
<body>
    <center>
        <h1><b><ins>Jungle Gym</ins></b></h1>
        <hr>
        <h2>Welcome to Jungle Gym where you can learn several different kinds of unarmed fighting styles along with their history and culture</h2>
        <br>
        <h1><b><ins>TRADITIONAL</ins></b></h1>
        <h4>This type of martial art means that it is still mostly unchanged and conforms more to its roots than keeping up with the times.</h4>
        <br>
        <h1>MUAY THAI</h1>
        <img src="muaythai.png">
        <h3>This martial art that originated in Thailand and was created in the 13th to 16th mainly to train soldiers for war if they were to ever be unarmed until in the 17th to 18th century it became a sort of entertainemnt 
        and even a part of royal festivals as this also goes by the other of "the art of 8 limbs" encompasing both pairs of legs, knees, fists, and elbows as its primary weapons for combat.</h3>
        <br>
        <h1>KARATE</h1>
        <img src="karate.png">
        <h3>In the nation of Japan or more specifically in the southern island of okinawa during the 13th to 17th century is when and where this martial art was born as it was heavily inspired by chinese martial arts but then diverged
        and became its own distinct fighting style as it focuses a heavy emphasis on its forms of "katas" with its main purpose being a more strike based martial art as it was adopted by the samurai and the shogunate during the edo period of japan's history.</h3>
        <br>
        <h1>JIU-JITSU</h1>
        <img src="JJT.png">
        <h3>Staying in the theme of japan Jiu-Jitsu was also created in this nation during the sengoku period also known as "the period of non stop war" from 1467 to 1600 century with its main purpose is pinning, choking, throwing the opponent away and
        while there is also another version of Jiu-Jitsu called Brazillian Jiu-Jitsu that is a actually a branching style that is completely distinct from the original as it blends other matrial arts in it as well.</h3>
        <br>
        <h1>TAE KWON DO</h1>
       <img src="TKD.png">
        <h3>Still on the eastern side of the world this time Korea Tae Kwon do is surprisingly very old but at the same time not as it is actually an evolution on another korean martial art called "Taekkyeon" that was 2000+ years old as it incorporated both arms and legs in its style of fighting and was further
        developed in the 13th to 19th century as it became more solely reliant on its legs and almost ditching the arms altogether with this art having two versions ITF the more traditional way of the art and WT a more dynamic and sports based way of the art.</h3>
        <br>
        <h1><b><ins>MODERN</ins></b></h1>
        <h4>The martial arts in this section is what can be best decribed as kept up to date or has had constant updates to its systems and still continues to change as time goes on.</h4>
        <br>
        <h1>BOXING</h1>
        <img src="BOXING.png">
        <h3>Moving on westward side of the globe with arguably the most famous and iconic martial art in human history that being boxing as it dates back to 3000 BCE and probably even older as it was used by the mesopotamians, egyptians, minoans, greeks, romans even making it to modern times as it is still
        widely used and known with its primary tool of conbat are the arms as it is majority punches that varies from jabs, hooks, cross's, feints, straights, and cuts additionally because it has been in the game for so long it was refularly developed or updated in each time period it was in especially
        today as it has not stopped evolving for thousands of years as in the 18th to 19th century they implemented footwork into its style and later on in 1910 to 1930 techniques called rolls, slips, and counters were added into the mix and on 1940's to 60's different kinds of guards and defenses came
        to see the light of day and in the following decades it was improvements after improvements with techniques to optimization to surprise attacks and even baiting became part of the arsenal in boxing.</h3>
        <br>
        <h1>KICK BOXING</h1>
         <img src="Kickboxing.png">
        <h3>This is a branching style from the iconic art of boxing as the main difference between the two is that in Kick boxing using the legs to strike and make contact with the opponent is unsuprisingly implemented in this divergent version of boxing as it is actually a micture of several other martial arts
        the obvious main one being boxing as it is followed up by muay thai and karate with a little bit of tae kwon do in the mix as this is also rather new being conceived in the 1960's but quickly became rather effective with its popularity also really fast and wide reaching because of its very dynamic 
        nature and adaptability as well as efficiency it reached global recognition and acclaim in record time as it spread to America, Europe, and Asia in just decades after being born.</h3>
        <br>
        <h1>GRAPPLING</h1>
        <img src="grappling.png">
        <h3>Also dating back thousands of years this martial art has many different origins and people that created and used this art through out history from Europe to asia and even the middle east there have been records of this art being used by the peoples of those regions and during different periods of time 
        as it is very mich about ground control and manipulating ones opponent because it utilizes pins, chokes, locks, binds, throws, clinches, holds, mountings, and ground rolls as it is also a sort of a hybrid martial art with the current version of grapling being a mixture of judo, sambo, jiu-jitsu, 
        and many other complimenting martial art that synergizes well with close ground combat.</h3>
        <br>
        <h1>WRESTLING</h1>
        <img src="wrestling.png">
        <h3>This also can falls under the umbrella term of grappling as it utilizes the basically the same fundamentals, principals, and movesets even history as well the only difference being this was made to be more of an actually showman ship of talent and skil inshort it was made for entertainment and for sport 
        as it has actually remained that way even until now with wrestling being a rather famous occupation and wrestlers also gaining noteriaty in the public eye because of how flashy and dynamic they are in their movements as they are quite litterally putting on a show to entertain the audience while still 
        showing off their capabilities.</h3>
        <br>
        <div><a href="{{ url_for('initial') }}"><button style="background-color:gray;color:red">Return to first page</button></a></div>
    </center>
</body>
</html>
"""

# Login page
login_html = """
<html>
<head>
    <title>Login Page</title>
    <style>{{ style }}</style>
</head>
<body>
    <center>
        <h2><b>Welcome to Jungle Gym. Please type in your name, password, and email to register.</b></h2>
        <hr>
        <form method="POST">
            <h3>If you already have an account, sign in here:</h3>
            <div><label>Name:</label><input type="text" name="login_name" placeholder="Tom Cruise"></div><br>
            <div><label>Password:</label><input type="password" name="login_pass" placeholder="Lord123"></div><br>
            <div><input type="submit" name="login" value="Sign In"></div><br>
            <hr>
        </form>
        <form method="POST">
            <h3>If you want to register as a member:</h3>
            <div><label>Name:</label><input type="text" name="reg_name" placeholder="Keanu Reeves"></div><br>
            <div><label>Password:</label><input type="password" name="reg_pass" placeholder="Jesus777"></div><br>
            <div><label>Email:</label><input type="text" name="reg_email" placeholder="example@gmail.com"></div><br>
            <div><input type="submit" name="register" value="Register"></div>
        </form>
        <br>
        <div><a href="{{ url_for('initial') }}"><button style="background-color:black;color:red">Return to first page</button></a></div>
    </center>
</body>
</html>
"""

# Members page
members_html = """
<html>
<head>
    <title>Members</title>
    <style>{{ style }}</style>
</head>
<body>
    <center>
        <h3><b>List of members and their Belt rankings in each martial art</b></h3>
        <table bgcolor="black" width="700">
            <tr bgcolor="grey" align="center">
                <th>Name</th><th>Wrestling</th><th>Grappling</th><th>Boxing</th><th>Kick Boxing</th>
                <th>Taek Won Do</th><th>Muay Thai</th><th>Karate</th><th>Jiu Jitsu</th>
            </tr>
            {% for member in members %}
            <tr bgcolor="lightgrey" align="center">
                <td>{{ member.name }}</td><td>{{ member.wrestling }}</td><td>{{ member.grappling }}</td>
                <td>{{ member.boxing }}</td><td>{{ member.kickboxing }}</td><td>{{ member.taekwondo }}</td>
                <td>{{ member.muaythai }}</td><td>{{ member.karate }}</td><td>{{ member.jiujitsu }}</td>
            </tr>
            {% endfor %}
        </table>
        <br>
        <div><a href="{{ url_for('info') }}"><button style="background-color:gray;color:red">Return to info page</button></a></div>
        <br>
        <div><a href="{{ url_for('login') }}"><button style="background-color:gray;color:blue">Return to login page</button></a></div>
    </center>
</body>
</html>
"""

# Store members in memory
members_list = []

# Routes
@app.route("/")
def initial():
    return render_template_string(initial_html, style=style_css)

@app.route("/info")
def info():
    return render_template_string(info_html, style=style_css)

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        if "register" in request.form:
            # Register new member
            members_list.append({
                "name": request.form["reg_name"],
                "wrestling": "blank",
                "grappling": "blank",
                "boxing": "blank",
                "kickboxing": "blank",
                "taekwondo": "blank",
                "muaythai": "blank",
                "karate": "blank",
                "jiujitsu": "blank"
            })
        return redirect(url_for('members'))
    return render_template_string(login_html, style=style_css)

@app.route("/members")
def members():
    return render_template_string(members_html, style=style_css, members=members_list)

if __name__ == "__main__":
    app.run(debug=True)

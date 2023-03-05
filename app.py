from flask import Flask, request, render_template
import stories



app = Flask(__name__)

@app.route('/')
def show_homepage():
    return render_template('home.html')

@app.route('/template')
def show_template():
    template_num = int(request.args['template_type'])
    story = stories.story_options[template_num]
    return render_template('lib_template.html', prompts=story.prompts, template_num=template_num)

@app.route('/story/<story_num>')
def print_story(story_num):
    story = stories.story_options[int(story_num)]
    prompts = story.prompts
    answers = {}
    
    print(type(prompts))
    for i in list(range(0, (len(prompts)))):
        answers[prompts[i]] = request.args[f'{prompts[i]}']
        
    print(answers)

    full_story = story.generate(answers)
   
    return render_template('story.html', story = full_story)
    


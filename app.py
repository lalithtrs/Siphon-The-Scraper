from bose.launch_tasks import launch_tasks
from bose import LocalStorage
from src import tasks_to_be_run, config
from flask import Flask, request, jsonify
import re
app = Flask(__name__)


@app.route('/add_query', methods=['POST'])
def add_query():

    print("Received request")
  
    try:
      query = request.get_json()['query']
  
      print("Query:", query)


      with open('src/config.py') as f:
          config = f.read()

      import re
      matches = re.findall(r'queries = (.*)', config)
      if matches:
          queries = eval(matches[0])  
      else:
          queries = []

      new_query = {"keyword": query}
      queries.append(new_query)

      new_config = re.sub(r'queries = .*', 
                        f'queries = {queries}', 
                        config)

      with open('src/config.py', 'w') as f:
        f.write(new_config)

    except Exception as e:
       print("Error:", e)
       return {"error": str(e)}

    return {"message": "Success"}

@app.route('/keywords')
def get_keywords():
  return jsonify(config.queries)

import re

@app.route('/start', methods=['POST'])
def start_scraper():

  launch_tasks(*tasks_to_be_run)
  count = LocalStorage.get_item('count', 0)
  return {"status": "Completed"}

if __name__ == "__main__":
    app.run()

from flask import Flask, request, jsonify
from models import db, Task
import os




def create_app(testing: bool = False) -> Flask:
    app = Flask(__name__)
  
  
    # Config
    app.config["SQLALCHEMY_DATABASE_URI"] = (
        "sqlite:///:memory:" if testing else os.getenv("DATABASE_URL", "sqlite:///tasks.db")
    )
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    
    
    db.init_app(app)
    
    
    with app.app_context():
        db.create_all()
    
    
    @app.get("/health")
    def health():
        return {"status": "ok"}, 200
    
    
    @app.post("/tasks")
    def create_task():
        data = request.get_json(silent=True) or {}
        title = data.get("title")
        if not title:
            return {"error": "'title' is required"}, 400
        task = Task(title=title)
        db.session.add(task)
        db.session.commit()
        return jsonify(task.to_dict()), 201
    
    
    @app.get("/tasks")
    def list_tasks():
        tasks = Task.query.order_by(Task.created_at.desc()).all()
        return jsonify([t.to_dict() for t in tasks]), 200
    
    
    @app.put("/tasks/<int:task_id>")
    def complete_task(task_id: int):
        task = Task.query.get(task_id)
        if not task:
            return {"error": "Task not found"}, 404
        data = request.get_json(silent=True) or {}
        if "title" in data:
            task.title = data["title"]
        if "completed" in data:
            task.completed = bool(data["completed"])
        else:
            task.completed = True
        db.session.commit()
        return jsonify(task.to_dict()), 200
        
    
    @app.delete("/tasks/<int:task_id>")
    def delete_task(task_id: int):
        task = Task.query.get(task_id)
        if not task:
            return {"error": "Task not found"}, 404
        db.session.delete(task)
        db.session.commit()
        return "", 204
    
    
    return app
    
    
    
if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 5000)))

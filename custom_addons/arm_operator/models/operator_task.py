from odoo import models, fields

class OperatorTask(models.Model):
    _name = "operator.task"
    _description = "Operator Task"

    name = fields.Char(string="Название задания", required=True)
    status = fields.Selection([
        ("ready", "Готово к работе"),
        ("in_progress", "В работе"),
        ("done", "Выполнено"),
        ("reject", "Брак"),
    ], default="ready", string="Статус")
    start_time = fields.Datetime(string="Начало")
    end_time = fields.Datetime(string="Окончание")

    def action_start_work(self):
        """Переводим задачу в работу"""
        for task in self:
            if task.status == "ready":
                task.status = "in_progress"
                task.start_time = fields.Datetime.now()

    def action_done(self):
        for task in self:
            if task.status == "in_progress":
                task.status = "done"
                task.end_time = fields.Datetime.now()

    def action_reject(self):
        for task in self:
            if task.status == "in_progress":
                task.status = "reject"
                task.end_time = fields.Datetime.now()

    def action_open_details(self):
        return {
            "type": "ir.actions.act_window",
            "res_model": "operator.task",
            "view_mode": "form",
            "res_id": self.id,
            "target": "current",
        }

    def action_open_files(self):

        return {
            "type": "ir.actions.act_window",
            "res_model": "ir.attachment",
            "view_mode": "kanban,tree,form",
            "domain": [("res_model", "=", "operator.task"), ("res_id", "=", self.id)],
            "context": {"default_res_model": "operator.task", "default_res_id": self.id},
            "target": "current",
        }




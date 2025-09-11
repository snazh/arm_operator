from odoo.tests import TransactionCase, tagged
import sys

# хелпер для логов со статусами
def log(msg, ok=True):
    icon = "✅" if ok else "❌"
    sys.stdout.write(f"{icon} {msg}\n")


@tagged('standard', 'at_install')
class TestOperatorTask(TransactionCase):

    def setUp(self):
        super().setUp()
        self.task = self.env["operator.task"].create({"name": "Тестовое задание"})
        log("Создана тестовая задача")

    def test_start_work(self):
        """Проверяю, что таска реально уходит в in_progress"""
        self.task.action_start_work()
        # тут статус должен быть "in_progress", иначе фэйл
        self.assertEqual(
            self.task.status, "in_progress",
            "❌ Статус не стал in_progress"
        )
        log("Статус изменился на in_progress")
        self.assertTrue(
            self.task.start_time,
            "❌ Время начала не установлено"
        )
        log("Время начала работы установлено")

    def test_done(self):
        """После старта таска должна нормально закрываться в done"""
        self.task.action_start_work()
        self.task.action_done()
        self.assertEqual(self.task.status, "done", "❌ Статус не стал done")
        log("Статус изменился на done")
        # end_time тоже обязан быть
        self.assertTrue(self.task.end_time, "❌ Время окончания не установлено")
        log("Время окончания установлено")

    def test_reject(self):
        """Чекаем reject после старта"""
        self.task.action_start_work()
        self.task.action_reject()
        self.assertEqual(self.task.status, "reject", "❌ Статус не стал reject")
        log("Статус изменился на reject")
        self.assertTrue(self.task.end_time, "❌ Время окончания не установлено")
        log("Время окончания установлено")

    def test_open_details_action(self):
        """action_open_details должен вернуть валидный action"""
        action = self.task.action_open_details()
        self.assertEqual(action["res_model"], "operator.task")
        self.assertEqual(action["res_id"], self.task.id)
        self.assertEqual(action["type"], "ir.actions.act_window")
        log("action_open_details возвращает корректное действие")

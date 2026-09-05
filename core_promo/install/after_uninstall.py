from core_promo.core_promo.customization.task.custom_field import delete_task_types


def after_install():
	delete_task_types()

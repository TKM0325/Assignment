from flask_appbuilder import ModelView
from flask_appbuilder.fieldwidgets import Select2Widget
from flask_appbuilder.models.sqla.interface import SQLAInterface
from .models import Employee,Department, Function, EmployeeHistory, Benefit, MenuItem, MenuCategory, News, NewsCategory, Comment, CommentCategory
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from app import appbuilder, db
from flask_appbuilder.baseviews import expose, BaseView


def department_query():
    return db.session.query(Department)


class EmployeeHistoryView(ModelView):
    datamodel = SQLAInterface(EmployeeHistory)
    #base_permissions = ['can_add', 'can_show']
    list_columns = ['department', 'begin_date', 'end_date']


class EmployeeView(ModelView):
    datamodel = SQLAInterface(Employee)

    list_columns = ['full_name', 'department.name', 'employee_number']
    edit_form_extra_fields = {'department':  QuerySelectField('Department',
                                query_factory=department_query,
                                widget=Select2Widget(extra_classes="readonly"))}


    related_views = [EmployeeHistoryView]
    show_template = 'appbuilder/general/model/show_cascade.html'


class FunctionView(ModelView):
    datamodel = SQLAInterface(Function)
    related_views = [EmployeeView]


class DepartmentView(ModelView):
    datamodel = SQLAInterface(Department)
    related_views = [EmployeeView]


class BenefitView(ModelView):
    datamodel = SQLAInterface(Benefit)
    add_columns = ['name']
    edit_columns = ['name']
    show_columns = ['name']
    list_columns = ['name']

class MenuItemView(ModelView):
    datamodel = SQLAInterface(MenuItem)
    list_columns = ['id', 'name', 'link', 'menu_category_id']

class MenuCategoryView(ModelView):
    datamodel = SQLAInterface(MenuCategory)
    list_columns = ['id', 'name']

class NewsView(ModelView):
    datamodel = SQLAInterface(News)
    list_columns = ['id', 'title', 'content', 'date', 'newsCat_id']

class NewsCategoryView(ModelView):
    datamodel = SQLAInterface(NewsCategory)
    list_columns = ['id', 'name']

class CommentView(ModelView):
    datamodel = SQLAInterface(Comment)
    list_columns = ['id', 'title', 'content', 'date', 'commentCat_id']
    
class CommentCategoryView(ModelView):
    datamodel = SQLAInterface(CommentCategory)
    list_columns = ['id', 'name']

class NewsPageView(BaseView):
    default_view = 'HongKong_News'
        
    @expose('/HongKong/')
    def HongKong_News(self):
        param1 = 'HONG KONG'
        self.update_redirect()
        return self.render_template('HongKongNews.html', param1=param1)
        
    @expose('/Asia/')
    def Asia_News(self):
        param1 = 'ASIA'
        self.update_redirect()
        return self.render_template('Asia.html', param1=param1)
        
    @expose('/Business/')
    def Buniness_News(self):
        param1 = 'BUSINESS'
        self.update_redirect()
        return self.render_template('Business.html', param1=param1)
        
    @expose('/Tech/')
    def Tech_News(self):
        param1 = 'TECH'
        self.update_redirect()
        return self.render_template('Tech.html', param1=param1)
        
    @expose('/Sport/')
    def Sport_News(self):
        param1 = 'SPORT'
        self.update_redirect()
        return self.render_template('Sport.html', param1=param1)
        
class CommentPageView(BaseView):
    default_view = 'SCMP_Editorials'
     
    @expose('/SCMP_Editorials/')
    def SCMP_Editorials(self):
        param1 = 'SCMP Editorials'
        self.update_redirect()
        return self.render_template('SCMP_Ed.html', param1=param1)
        
    @expose('/Opinion/')
    def Opinion(self):
        param1 = 'Opinion'
        self.update_redirect()
        return self.render_template('Opinion.html', param1=param1)
        
    @expose('/Harry''s View/')
    def HarryView(self):
        param1 = 'Harry''s View'
        self.update_redirect()
        return self.render_template('HV.html', param1=param1)

    @expose('/Letter/')
    def Letter(self):
        param1 = 'Letter'
        self.update_redirect()
        return self.render_template('Letter.html', param1=param1)


db.create_all()

""" Page View """
appbuilder.add_view(NewsPageView, 'Hong Kong', category="News")
appbuilder.add_link("Asia", href="/newspageview/Asia/", category="News")
appbuilder.add_link("Business", href="/newspageview/Business/", category="News")
appbuilder.add_link("Tech", href="/newspageview/Tech/", category="News")
appbuilder.add_link("Sport", href="/newspageview/Sport/", category="News")


appbuilder.add_view(CommentPageView, 'SCMP_Editorials', category="Comment")
appbuilder.add_link("Opinion", href="/commentpageview/Opinion/", category="Comment")
appbuilder.add_link("Harry''s View", href="/commentpageview/Harry''s View/", category="Comment")
appbuilder.add_link("Letter", href="/commentpageview/Letter/", category="Comment")

""" Custom Views """
appbuilder.add_view(MenuItemView, "MenuItem", icon="fa-folder-open-o", category="Admin")
appbuilder.add_view(MenuCategoryView, "MenuCategory", icon="fa-folder-open-o", category="Admin")
appbuilder.add_view(NewsView, "News", icon="fa-folder-open-o", category="Admin")
appbuilder.add_view(NewsCategoryView, "NewsCategory", icon="fa-folder-open-o", category="Admin")
appbuilder.add_view(CommentView, "Comment", icon="fa-folder-open-o", category="Admin")
appbuilder.add_view(CommentCategoryView, "CommentCategory", icon="fa-folder-open-o", category="Admin")
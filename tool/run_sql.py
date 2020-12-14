# 导入模块
import sqlite3


def run_sql(sql):
    # 创建连接
    global result
    con = sqlite3.connect(r'E:\CIMP\cimp\backend\db.sqlite3')
    # 创建游标对象
    cur = con.cursor()
    # 编写删除数据的SQL语句
    # sql = 'delete from t_person where pno=?'
    # 执行sql
    try:
        cur.execute(sql)  # 必须是元组类型（2 ,）
        result = cur.fetchall()
        # 提交事务
        con.commit()
        print("执行成功成功")
    except Exception as e:
        print(e)
        print("执行失败，回滚事务")
        con.rollback()
    finally:
        print(result)
        # 关闭游标
        cur.close()
        # 关闭连接
        con.close()

if __name__ == '__main__':
    run_sql('delete from cimp_wf_design where creator_id = 12 ')
    run_sql('delete from cimp_wf_design_step where operator_id = 12 or operator_id = 13')
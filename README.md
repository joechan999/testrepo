# testrepo

## Editing the file

Its a markdown file in this repository.

test123

如果有多个数据源，可以使用 Spring 提供的 ChainedTransactionManager 来处理事务。ChainedTransactionManager 是一个支持多个事务管理器的事务管理器，它可以将多个事务管理器链接在一起，以实现事务管理的功能。

以下是一个简单的 Spring 配置文件，展示如何配置多个数据源和 ChainedTransactionManager：

<bean id="dataSource1" class="org.apache.commons.dbcp2.BasicDataSource">
    <property name="driverClassName" value="com.mysql.jdbc.Driver" />
    <property name="url" value="jdbc:mysql://localhost:3306/db1" />
    <property name="username" value="root" />
    <property name="password" value="password" />
</bean>

<bean id="dataSource2" class="org.apache.commons.dbcp2.BasicDataSource">
    <property name="driverClassName" value="com.mysql.jdbc.Driver" />
    <property name="url" value="jdbc:mysql://localhost:3306/db2" />
    <property name="username" value="root" />
    <property name="password" value="password" />
</bean>

<bean id="transactionManager1" class="org.springframework.jdbc.datasource.DataSourceTransactionManager">
    <property name="dataSource" ref="dataSource1" />
</bean>

<bean id="transactionManager2" class="org.springframework.jdbc.datasource.DataSourceTransactionManager">
    <property name="dataSource" ref="dataSource2" />
</bean>

<bean id="chainedTransactionManager" class="org.springframework.transaction.support.ChainedTransactionManager">
    <property name="transactionManagers">
        <list>
            <ref bean="transactionManager1" />
            <ref bean="transactionManager2" />
        </list>
    </property>
</bean>

<bean id="myService" class="com.example.MyService">
    <property name="dataSource1" ref="dataSource1" />
    <property name="dataSource2" ref="dataSource2" />
</bean>

在上面的配置文件中，我们配置了两个数据源 dataSource1 和 dataSource2，以及两个对应的事务管理器 transactionManager1 和 transactionManager2。接着，我们使用 ChainedTransactionManager 将这两个事务管理器链接在一起，创建一个新的事务管理器 chainedTransactionManager。最后，我们配置了一个 MyService 的 bean，这个 bean 中使用了 dataSource1 和 dataSource2。

下面是一个使用 ChainedTransactionManager 的示例代码：

java
Copy code
@Service
public class MyService {

    private final JdbcTemplate jdbcTemplate1;
    private final JdbcTemplate jdbcTemplate2;

    public MyService(DataSource dataSource1, DataSource dataSource2) {
        this.jdbcTemplate1 = new JdbcTemplate(dataSource1);
        this.jdbcTemplate2 = new JdbcTemplate(dataSource2);
    }

    @Transactional
    public void doTransaction() {
        jdbcTemplate1.update("INSERT INTO mytable1 (name) VALUES (?)", "John");
        jdbcTemplate2.update("INSERT INTO mytable2 (name) VALUES (?)", "Doe");
    }

}
在上面的示例代码中，我们使用了 @Transactional 注解来标注 doTransaction 方法，这意味着这个方法中的 SQL 操作会被视为一个事务，并由 chainedTransactionManager 进行管理。如果这个方法中

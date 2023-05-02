# Display the output
print("New Python file")


当存在多个数据源时，我们可以配置多个 Transaction Manager，每个 Transaction Manager 关联一个数据源。在进行事务处理时，我们需要显式地指定使用哪个 Transaction Manager。

以下是一个简单的 Spring 配置文件，展示如何配置两个数据源和对应的 Transaction Manager：

xml
Copy code
<bean id="dataSource1" class="org.apache.commons.dbcp2.BasicDataSource">
    <property name="driverClassName" value="com.mysql.jdbc.Driver" />
    <property name="url" value="jdbc:mysql://localhost:3306/mydb1" />
    <property name="username" value="root" />
    <property name="password" value="password" />
</bean>

<bean id="dataSource2" class="org.apache.commons.dbcp2.BasicDataSource">
    <property name="driverClassName" value="com.mysql.jdbc.Driver" />
    <property name="url" value="jdbc:mysql://localhost:3306/mydb2" />
    <property name="username" value="root" />
    <property name="password" value="password" />
</bean>

<bean id="transactionManager1" class="org.springframework.jdbc.datasource.DataSourceTransactionManager">
    <property name="dataSource" ref="dataSource1" />
</bean>

<bean id="transactionManager2" class="org.springframework.jdbc.datasource.DataSourceTransactionManager">
    <property name="dataSource" ref="dataSource2" />
</bean>

<bean id="myService1" class="com.example.MyService">
    <property name="dataSource" ref="dataSource1" />
</bean>

<bean id="myService2" class="com.example.MyService">
    <property name="dataSource" ref="dataSource2" />
</bean>
在上面的配置文件中，我们配置了两个数据源 dataSource1 和 dataSource2，以及对应的 Transaction Manager transactionManager1 和 transactionManager2。同时，我们也配置了两个 MyService 的 bean 分别使用不同的数据源。

下面是一个使用 Transaction Manager 处理多个数据源的示例代码：

java
Copy code
@Service
public class MyService {

    private final JdbcTemplate jdbcTemplate;

    public MyService(DataSource dataSource) {
        this.jdbcTemplate = new JdbcTemplate(dataSource);
    }

    @Transactional("transactionManager1")
    public void doTransaction1() {
        jdbcTemplate.update("INSERT INTO mytable1 (name) VALUES (?)", "John");
    }

    @Transactional("transactionManager2")
    public void doTransaction2() {
        jdbcTemplate.update("INSERT INTO mytable2 (name) VALUES (?)", "Doe");
    }

}
在上面的示例代码中，我们分别使用了 @Transactional("transactionManager1") 和 @Transactional("transactionManager2") 注解来标注 doTransaction1 和 doTransaction2 方法，明确指定了使用哪个 Transaction Manager。这样，在执行事务时，Spring 框架会根据注解中指定的 Transaction Manager 来管理对应的数据源。

总结来说，对于多个数据源，我们可以配置多个 Transaction Manager 来管理事务，使用 @Transactional 注解时需要明确指定使用哪个 Transaction Manager。
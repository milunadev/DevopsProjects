import boto3

# # Configuración de AWS
# aws_access_key_id = 'TU_ACCESS_KEY'
# aws_secret_access_key = 'TU_SECRET_KEY'
# region_name = 'TU_REGION'

# Etiqueta para filtrar
tag_key = 'name'
tag_value = 'vprofile'

# Crea clientes de AWS para cada servicio
ec2 = boto3.client('ec2')
elb = boto3.client('elbv2')
r53 = boto3.client('route53')


# Función para obtener instancias EC2
def get_ec2_instances():
    instances = []
    paginator = ec2.get_paginator('describe_instances')
    for page in paginator.paginate(Filters=[{'Name': 'tag:' + tag_key, 'Values': [tag_value]}]):
        for reservation in page['Reservations']:
            for instance in reservation['Instances']:
                instances.append(instance['InstanceId'])
    return instances

# Función para obtener Load Balancers
def get_load_balancers():
    load_balancers = []
    paginator = elb.get_paginator('describe_load_balancers')
    for page in paginator.paginate():
        for lb in page['LoadBalancers']:
            # Aquí debes implementar la lógica para filtrar por etiqueta
            # Ya que la API de ELB maneja las etiquetas de manera diferente
            load_balancers.append(lb['LoadBalancerArn'])
    return load_balancers

# Añade aquí las funciones para obtener Security Groups y DNS Zones




# Función para eliminar instancias EC2
def delete_ec2_instances(instance_ids):
    if instance_ids:
        print(f"Terminando instancias EC2: {instance_ids}")
        ec2.terminate_instances(InstanceIds=instance_ids)

# Función para eliminar Load Balancers
def delete_load_balancers(lb_arns):
    for lb_arn in lb_arns:
        print(f"Eliminando Load Balancer: {lb_arn}")
        elb.delete_load_balancer(LoadBalancerArn=lb_arn)

# Añade aquí las funciones para eliminar Security Groups y DNS Zones


# Obtén los recursos
instances = get_ec2_instances()
load_balancers = get_load_balancers()
# Añade aquí las llamadas para obtener Security Groups y DNS Zones

# Elimina los recursos
delete_ec2_instances(instances)
delete_load_balancers(load_balancers)
# Añade aquí las llamadas para eliminar Security Groups y DNS Zones

import torch
from gpugym.envs.base.legged_robot_config \
    import LeggedRobotCfg, LeggedRobotCfgPPO

class test_config(LeggedRobotCfg):
    class env(LeggedRobotCfg.env):
        num_envs = 4096
        num_observations = 211
        num_actions = 14
        episode_length_s = 70
        num_history_short = 3

    class terrain(LeggedRobotCfg.terrain):
        curriculum = False
        mesh_type =  'plane' # 'trimesh'
        measure_heights = False
        static_friction = 0.1
        dynamic_friction = 0.1

    class commands(LeggedRobotCfg.commands):
        curriculum = False
        max_curriculum = 1.
        num_commands = 4
        resampling_time = 5.
        robot_height_command = True
        ang_vel_command = True
        #-------------------------------------------
        lin_vel_clip = 0.3
        ang_vel_yaw_clip = 0.2
        static_delay = 50.
        resampling_range = [3., 15.] # for random resample time

        class ranges:
            # TRAINING COMMAND RANGES #
            lin_vel_x = [-1.5, 1.5]        # min max [m/s]
            lin_vel_y = [-0.6, 0.6]   # min max [m/s]
            ang_vel_yaw = [-1., 1.]     # min max [rad/s]
            robot_height = [0.5, 1.]     # min max [scale]

    class init_state(LeggedRobotCfg.init_state):
        reset_mode = 'reset_to_range'
        penetration_check = False
        pos = [0., 0., 0.75]        # x,y,z [m]  
        rot = [0.0, 0.0, 0.0, 1.0]  # x,y,z,w [quat]
        lin_vel = [0.0, 0.0, 0.0]   # x,y,z [m/s]
        ang_vel = [0.0, 0.0, 0.0]   # x,y,z [rad/s]

        # ranges for [x, y, z, roll, pitch, yaw]
        root_pos_range = [
            [0., 0.],
            [0., 0.],
            [0.7, 0.7],      
            [-torch.pi/10, torch.pi/10],
            [-torch.pi/10, torch.pi/10],
            [-torch.pi/10, torch.pi/10]
        ]

        # ranges for [v_x, v_y, v_z, w_x, w_y, w_z]
        root_vel_range = [
            [-.5, .5],
            [-.5, .5],
            [-.5, .5],
            [-.5, .5],
            [-.5, .5],
            [-.5, .5]
        ]

        default_joint_angles = {
            'r_hip_pitch_joint': 0.0,
            'r_hip_roll_joint': 0.0,
            'r_hip_yaw_joint': 0.0,
            'r_knee_joint': 0.0,
            'r_ankle_pitch_joint': 0.0,
            'r_ankle_roll_joint': 0.0,
            
            'l_hip_pitch_joint': 0.0,
            'l_hip_roll_joint': 0.0,
            'l_hip_yaw_joint': 0.0,
            'l_knee_joint': 0.0,
            'l_ankle_pitch_joint': 0.0,
            'l_ankle_roll_joint': 0.0,
            'rarm_joint1': 0.0,
            'larm_joint1': 0.0,
            
        }

        dof_pos_range = {
            'r_hip_pitch_joint': [-1.0, 2.0],
            'r_hip_roll_joint': [-0.2, 0.2],
            'r_hip_yaw_joint': [-0.4, 0.4],
            'r_knee_joint': [-1.2, 0.0],
            'r_ankle_pitch_joint': [-0.3, 0.3],
            'r_ankle_roll_joint': [-0.3, 0.3],
            
            'l_hip_pitch_joint': [-1.0, 2.0],
            'l_hip_roll_joint': [-0.2, 0.2],
            'l_hip_yaw_joint': [-0.4, 0.4],
            'l_knee_joint': [-1.2, 0.0],
            'l_ankle_pitch_joint': [-0.3, 0.3],
            'l_ankle_roll_joint': [-0.3, 0.3],
                                    
            'rarm_joint1': [-0.3,0.3],
            'larm_joint1': [-0.3,0.3],

        }

        dof_vel_range = {
            'r_hip_pitch_joint': [-0.1, 0.1],
            'r_hip_roll_joint': [-0.1, 0.1],
            'r_hip_yaw_joint': [-0.1, 0.1],
            'r_knee_joint': [-0.1, 0.1],
            'r_ankle_pitch_joint': [-0.1, 0.1],
            'r_ankle_roll_joint': [-0.1, 0.1],
            
            'l_hip_pitch_joint': [-0.1, 0.1],
            'l_hip_roll_joint': [-0.1, 0.1],
            'l_hip_yaw_joint': [-0.1, 0.1],
            'l_knee_joint': [-0.1, 0.1],
            'l_ankle_pitch_joint': [-0.1, 0.1],
            'l_ankle_roll_joint': [-0.1, 0.1],
            
            'rarm_joint1': [-0.1,0.1],
            'larm_joint1': [-0.1,0.1],
        }

    class control(LeggedRobotCfg.control):
        control_type = 'P' # P: position, V: velocity, T: torques
        # stiffness and damping for joints
        stiffness = {
            'r_hip_pitch_joint': 75.,
            'r_hip_roll_joint': 50.,
            'r_hip_yaw_joint': 50.,
            'r_knee_joint': 75.,
            'r_ankle_pitch_joint': 30.,
            'r_ankle_roll_joint': 15.,
            
            'l_hip_pitch_joint': 75.,
            'l_hip_roll_joint': 50.,
            'l_hip_yaw_joint': 50.,
            'l_knee_joint': 75.,
            'l_ankle_pitch_joint': 30.,
            'l_ankle_roll_joint': 15.,
            
            'rarm_joint1': 75.,
            'larm_joint1': 75.,
        }
        damping = {
            'r_hip_pitch_joint': 6.,
            'r_hip_roll_joint': 3.,
            'r_hip_yaw_joint': 3.,
            'r_knee_joint': 6.,
            'r_ankle_pitch_joint': 2.,
            'r_ankle_roll_joint': 1.,
            
            'l_hip_pitch_joint': 6.,
            'l_hip_roll_joint': 3.,
            'l_hip_yaw_joint': 3.,
            'l_knee_joint': 6.,
            'l_ankle_pitch_joint': 2.,
            'l_ankle_roll_joint': 1.,
        
            'rarm_joint1': 6.,
            'larm_joint1': 6.,
        }

        action_scale = 1.0
        exp_avg_decay = 0.05
        decimation = 20

    class domain_rand(LeggedRobotCfg.domain_rand):
        randomize_friction = True
        # friction_range = [0.5, 1.25]
        friction_range = [0.3, 3.]

        #old mass randomize
        randomize_base_mass = False
        added_mass_range = [-1., 1.]

        randomize_all_mass = True
        rd_mass_range = [0.5, 1.5]

        randomize_com = True
        rd_com_range = [-0.05, 0.05]

        randomize_base_com = True
        rd_base_com_range = [-0.1, 0.1]
        
        
        push_robots = True
        push_interval_s = 2
        push_ratio= 0.4
        max_push_vel_xy = 0.5
        max_push_ang_vel = 0.4

        random_pd = True
        p_range = [0.7, 1.3]
        d_range = [0.7, 1.3]

        random_damping = True
        damping_range = [0.3, 4.0]

        random_inertia = True
        inertia_range = [0.7, 1.3]

        comm_delay = False
        comm_delay_range = [0, 11] # will exclude the upper limit

    class asset(LeggedRobotCfg.asset):
        file = '{LEGGED_GYM_ROOT_DIR}'\
            '/resources/robots/orcai_description/urdf/orca_description_mj.urdf'
        keypoints = ["base_link"]
        end_effectors = ['r_ankle_roll_link', 'l_ankle_roll_link']
        foot_name = ['l_ankle_roll_link', 'r_ankle_roll_link']
        terminate_after_contacts_on = [
            "base_link",
            "l_hip_yaw_link",
            "r_hip_yaw_link"
        ]

        disable_gravity = False
        disable_actions = False
        disable_motors = False

        # (1: disable, 0: enable...bitwise filter)
        self_collisions = 0
        collapse_fixed_joints = False
        flip_visual_attachments = False

        # Check GymDofDriveModeFlags
        # (0: none, 1: pos tgt, 2: vel target, 3: effort)
        default_dof_drive_mode = 3

    class rewards(LeggedRobotCfg.rewards):
        # ! "Incorrect" specification of height
        base_height_target = 0.7
        # base_height_target = 2.0
        soft_dof_pos_limit = 0.9
        soft_dof_vel_limit = 0.9
        soft_torque_limit = 0.8
        max_contact_force = 1500.
        target_joint_pos_scale = 0.50    # rad
        target_feet_height = 0.15        # m
        cycle_time = 1.0                # sec
        # negative total rewards clipped at zero (avoids early termination)
        only_positive_rewards = False
        tracking_sigma = 0.5

        class scales(LeggedRobotCfg.rewards.scales):
            # * "True" rewards * #
            # reward for task
            tracking_lin_vel = 10.
            tracking_ang_vel = 5.
            joint_pos = 1.6
            feet_clearance = 1.
            feet_contact_number = 1.2
            no_fly = 1.0
            no_jump = 1.0
            stand_still = 1.0
            feet_air_time = 1.0

            foot_slip = 0.5

            # reward for smooth
            action_rate = -1.e-6
            action_rate2 = -1.e-6
            torques = -1e-6
            base_lin_acc = -1e-3
            base_ang_acc = -2e-5
            ##############################
            dof_acc = -4e-4
            dof_vel = -1e-4

            #reward for safety
            dof_pos_limits = -10
            torque_limits = -1e-2
            feet_contact_forces = -5e-3
            termination = -100
            
            # ang_vel_xy = -5.
            # lin_vel_z = -5.
            
            #reward for beauty
            # * Shaping rewards * #
            # Sweep values: [0.5, 2.5, 10, 25., 50.]
            # Default: 5.0
            # orientation = 5.0

            # Sweep values: [0.2, 1.0, 4.0, 10., 20.]
            # Default: 2.0
            base_height = 2.0

            # Sweep values: [0.1, 0.5, 2.0, 5.0, 10.]
            # Default: 1.0
            joint_regularization = 1.0
            ankle_regularization = 1.0
            # * PBRS rewards * #
            # Sweep values: [0.1, 0.5, 2.0, 5.0, 10.]
            # Default: 1.0
            ori_pb = 1.0

            # Sweep values: [0.1, 0.5, 2.0, 5.0, 10.]
            # Default: 1.0
            baseHeight_pb = 0.3

            # Sweep values: [0.1, 0.5, 2.0, 5.0, 10.]
            # Default: 1.0
            jointReg_pb = 1.0

            # ankleReg_pb = 0.1


    class normalization(LeggedRobotCfg.normalization):
        class obs_scales(LeggedRobotCfg.normalization.obs_scales):
            base_z = 1./0.6565

        clip_observations = 100.
        clip_actions = 10.

    class noise(LeggedRobotCfg.noise):
        add_noise = True
        noise_level = 1.0  # scales other values

        class noise_scales(LeggedRobotCfg.noise.noise_scales):
            base_z = 0.05
            dof_pos = 0.002 # 0.005
            dof_vel = 0.001 # 0.01
            lin_vel = 0.04 # 0.1
            ang_vel = 0.05
            gravity = 0.002 # 0.05
            in_contact = 0.1
            height_measurements = 0.1

    class sim(LeggedRobotCfg.sim):
        dt = 0.001
        substeps = 1
        gravity = [0., 0., -9.81]

        class physx:
            max_depenetration_velocity = 10.0


class test_configPPO(LeggedRobotCfgPPO):
    do_wandb = True
    seed = -1

    class algorithm(LeggedRobotCfgPPO.algorithm):
        # algorithm training hyperparameters
        value_loss_coef = 1.0
        use_clipped_value_loss = True
        clip_param = 0.2
        entropy_coef = 0.01
        num_learning_epochs = 5
        num_mini_batches = 4    # minibatch size = num_envs*nsteps/nminibatches
        learning_rate = 1.e-5
        schedule = 'adaptive'   # could be adaptive, fixed
        gamma = 0.98
        lam = 0.95
        desired_kl = 0.01
        max_grad_norm = 1.
        weight_decay = 0

    class runner(LeggedRobotCfgPPO.runner):
        policy_class_name = 'ActorCritic'
        algorithm_class_name = 'PPO'
        num_steps_per_env = 24
        max_iterations = 30000
        run_name = ''
        experiment_name = 'XBot_ppo'
        save_interval = 50
        plot_input_gradients = False
        plot_parameter_gradients = False

    class policy(LeggedRobotCfgPPO.policy):
        actor_hidden_dims = [256, 256, 256]
        critic_hidden_dims = [256, 256, 256]
        # (elu, relu, selu, crelu, lrelu, tanh, sigmoid)
        activation = 'elu'
        conv_dims = [(42, 32, 6, 5), (32, 16, 4, 2)]
        period_length = 100
        
        
        
        
        
        
"""
Configuration file for cassie
"""





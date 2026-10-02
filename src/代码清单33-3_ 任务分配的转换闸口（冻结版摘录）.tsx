    transitionTo: (target, operator, operatorRole, comment) => {
      const state = get();
      const allowed = TRANSITIONS[state.status];
      if (!allowed.includes(target)) {
        set({ ...state, error: `非法转换：${state.status} → ${target}` });
        return;
      }
      // 复用 reducer 的权限校验路径
      const actionType = actionTypeForTarget(target);
      const requiredRole = ACTION_REQUIRED_ROLE[actionType];
      if (requiredRole && operatorRole && operatorRole !== requiredRole) {
        set({ ...state, error: `权限不足：${actionType} 需要 ${requiredRole} 角色` });
        return;
      }
      dispatch({
        type: actionType as FlowAction["type"],
        operator,
        operatorRole,
        comment,
      });
    },